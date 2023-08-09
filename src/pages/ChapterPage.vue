<template>
    <feed-container v-if="!loading">
      <disclaimer-message></disclaimer-message>    
      <div class="story-container">
        <div v-for="chapter in chapterList" :key="chapter._id">
          <template v-if="chapter.type === 'prologue'">
            <div class="main-title-container">
                <h2 class="main-title">{{ chapter.title.toUpperCase() }}</h2>
            </div>
            <div class="tag-section">
                <post-tag v-for="tag in chapter.tags" :key="tag" :clickable="false" :tag="tag"></post-tag>
            </div> 
            <div class="story-stats">
              <div class="story-stats-section">
                <span class="material-symbols-outlined margin1 leaf-icon" 
                      :class="[postData.leaves.includes(currentUser) ? 'includes-leaf-icon' : '']"
                      >nest_eco_leaf
                    </span>
                    {{ totalLeaves }} <!-- use postData.leaves.length for prologue stats only, or chapterList[chapterList.length - 1].leaves.length for last mounted chapter only-->
                </div>
                <div class="story-stats-section"><span class="material-symbols-outlined margin1">bar_chart</span>{{ postData.views }}</div>
                <div class="story-stats-section"><span class="material-symbols-outlined margin1">chat</span>{{ postData.user_comments.length }}</div>
                <div class="story-stats-section"><span class="material-symbols-outlined margin1">share</span></div>
            </div>   
            <chapteredprologue-container
              :_id="chapter._id"
              :content="chapter.content"
              :title="chapter.title"
              :username="chapter.username"
              :color="chapter.color"
              :postComment="chapter.comment"
              :date="chapter.date"
              :picture="chapter.picture"
              :feedMode="false"
              class="story__article1">
            </chapteredprologue-container>
          </template>
          <template v-else>
            <chaptered-container
              :_id="chapter._id"
              :storyId="chapter.story_id"
              :parentChapterId="chapter.parent_chapter_id"
              :content="chapter.content"
              :chapterName="chapter.chapter_name"
              :chapterNum="chapter.chapter_num"
              :username="chapter.username"
              :postComment="chapter.comment"
              :date="chapter.date"
              :picture="chapter.picture"
              class="story__article2">
            </chaptered-container>
          </template>
        </div>
        <span v-if="isLoggedIn">
          <div class="add-story-container" @click="toggleContinueContainer">
            <h2 class="add-story"> WRITE CHAPTER {{ chapterList[chapterList.length - 1].chapter_num + 1 }} FOR THIS STORYLINE</h2>
          </div>
          <writechapter-container
          v-if="showContinueContainer"
          :chapterNum="chapterList[chapterList.length - 1].chapter_num + 1"
          :username="currentUser"
          :postId="chapterList[0]._id"
          :postTitle="chapterList[0].title"
          :parentChapterId="chapterList[chapterList.length - 1]._id"
          :tags="chapterList[0].tags">
        </writechapter-container>
        </span>   
      </div>
      <div class="add-comment-box" v-if="isLoggedIn">
        <form @submit.prevent="submitComment">
            <div class="newstory_comment">
                <div class="image_box">
                    <img class="postimage" :src="imgSource" alt="profilepic">
                </div>
                <textarea id="comment" v-model="formcomment" placeholder="Add a comment..." rows="1" :style="{ height: textareaHeight }" required></textarea>
                <div class="buttonbox">
                  <button class="postbutton" type="submit">Comment</button>
                </div>
            </div>
        </form>
      </div>
      <div v-if="!isLoggedIn" class="alert alert-info mt-3 shadow p-2" role="alert">
        <b>Log in</b> to write comments and continue storylines
      </div>
      <span v-if="!loadingComments">
        <div v-for="reply in replies" :key="reply._id">
          <template v-if="reply.type === 'comment'">
            <comment-container
              :_id="reply._id"
              :content="reply.comment"
              :username="reply.username"
              :date="reply.date"
              :picture="reply.picture"
            ></comment-container>
          </template>
          <template v-else-if="reply.type === 'chapter' && !chapterList.some(obj => obj._id.$oid === reply._id.$oid)">
            <continuestory-container
              :_id="reply._id"
              :storyId="reply.story_id"
              :parentChapterId="reply.parent_chapter_id"
              :content="reply.content"
              :chapterName="reply.chapter_name"
              :chapterNum="reply.chapter_num"
              :username="reply.username"
              :postComment="reply.comment"
              :date="reply.date"
              :picture="reply.picture"
              :tags="reply.tags"
            ></continuestory-container>
          </template>
        </div>
        <astronaut-message v-if="replies.length == chapterList[chapterList.length - 1].chapter_num" class="imagecontainer"
        :onomatopoeia="'crick crick'"
        :text="'No comments or chapters have been written for this story yet. You can be the first, hurry up!'">
        </astronaut-message>
      </span>
      <div v-else class="loader-container" style="margin-top: -8px">
        <div class="spinner-border text-light mb-3" style="width: 5rem; height: 5rem;" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        <span class="loader-text">Harvesting comments from story...</span>
      </div>
    </feed-container>
    <feed-container v-else>
      <div class="loader-container">
        <div class="spinner-border text-light mb-3" style="width: 5rem; height: 5rem;" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        <span class="loader-text">Adding chapters to main story...</span>
      </div>
    </feed-container>
</template>

<script>
import axios from "axios";
import { API_BASE_URL } from '../config';
import { mapGetters } from 'vuex';

import DisclaimerMessage from "@/components/layout/messages/DisclaimerMessage.vue";
import FeedContainer from '@/components/layout/FeedContainer.vue';
import ChapteredContainer from "@/components/layout/ChapteredContainer.vue";
import ChapteredprologueContainer from "@/components/layout/ChapteredprologueContainer.vue";
import CommentContainer from "@/components/layout/CommentContainer.vue";
import ContinuestoryContainer from "@/components/layout/ContinuestoryContainer.vue";
import WritechapterContainer from "@/components/layout/WritechapterContainer.vue";
import AstronautMessage from "@/components/layout/messages/AstronautMessage.vue";
import PostTag from "@/components/layout/PostTag.vue";

export default {
  components: {
    FeedContainer,
    ChapteredContainer,
    ChapteredprologueContainer,
    CommentContainer,
    ContinuestoryContainer,
    WritechapterContainer,
    AstronautMessage,
    DisclaimerMessage,
    PostTag
  },
  data() {
    return {
      chapterList: null,
      formcomment: "",
      continuedStory: null,
      textareaHeight: null,
      loading: true,
      replies: [],
      loadingComments: true,
      showContinueContainer: false,
      postData: {},
      totalLeaves: 0
    }
  },
  mounted() {
    const chapterId = this.$route.params.id;
    axios
      .get(`${API_BASE_URL}/chapter/${chapterId}`)
      .then(response => {
        this.chapterList = response.data;
        this.loading = false;
        this.postData = this.chapterList[0];
        this.totalLeaves += this.postData.leaves.length;

        this.chapterList.forEach((chapter) => {
          this.totalLeaves += chapter.leaves.length;
        });
        axios
          .get(`${API_BASE_URL}/post/${this.postData._id.$oid}`)
          .then(response => {
            this.replies = response.data.replies;
            this.loadingComments = false;
          })
      })
      
  },
  computed: {
    ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched"]),
    imgSource() {
       return require("../assets/img/" + this.userFetchedPicture);
    }
  },
  methods: {
    adjustTextareaHeight() {
      const textarea = this.$el.querySelector('#comment');
      textarea.style.height = 'auto';
      textarea.style.height = textarea.scrollHeight + 'px';
      this.textareaHeight = textarea.style.height;
    },
    toggleContinueContainer() {
      this.showContinueContainer = !this.showContinueContainer
    },
    submitComment() {

      const data_packet = {
        username: this.currentUser,
        comment: this.formcomment,
        parentId: this.chapterList[0]._id.$oid
      }

      axios
        .post(`${API_BASE_URL}/new_comment`, data_packet)
        .then(response => {
          const dataPayload = response.data;

          this.replies.unshift(dataPayload.comment_data); // Add the new comment to the beginning of the replies array
          this.formcomment = ''; // Clear the comment input field
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  watch: {
    formcomment() {
          this.formcomment = this.formcomment.substring(0, 300);
          this.adjustTextareaHeight();
        },
  }
}
</script>

<style scoped>
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 200,
  'opsz' 48
}

.leaf {
    color: white;
    transition: all 0.1s;
}

.leaf-icon {
    color: rgb(0, 255, 106);
}

.leaf:hover .leaf-icon{
    color: rgb(0, 255, 106);
}

.includes-leaf {
    color: rgb(0, 255, 106);
}

.includes-leaf-icon {
    font-variation-settings:
    'FILL' 1,
    'wght' 400,
    'GRAD' 0,
    'opsz' 200
}
.tag-section {
    display: flex;
    justify-content: center;
    margin: -8px 7px 0px 7px;
    flex-wrap: wrap;
}
.separator {
    border-top: rgba(245, 245, 245, 0.075) 1px solid;
    width: 95%;
    margin: auto;
}

.story-stats {
    display: flex;
    color: whitesmoke;
    margin: 5px 5px 2px 5px;
    justify-content: center;
}

.story-stats-section {
    display: flex;
    align-items: center;
    margin: 0 12px;
    padding: 1px 6px 1px 1px;
}

.story-stats-section:hover {
    background-color: rgba(194, 194, 194, 0.137);
    border-radius: 10px;
}

.onomatopoeia {
    color: whitesmoke;
    font-weight: bold;
    font-size: 14px;
    margin-bottom: -10px;
}

@keyframes floatAnimation {
  0% {
    transform: translateY(-5px);
  }
  50% {
    transform: translateY(5px);
  }
  100% {
    transform: translateY(-5px);
  }
}

.astronaut-image {
    width: 175px;
    height: auto;
    animation: floatAnimation 4s ease-in-out infinite;
}

.imagecontainer {
    margin: 50px auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: fit-content;
}

.loader-text {
    background-color: whitesmoke;
    text-align: center;
    color: rgb(0, 0, 0);
    padding: 5px 10px;
    border-radius: 15px;
    font-weight: bold;
    margin: 0 10px;
}

.add-story-container {
    display: flex;
    margin: 5px 0 5px 0;
    justify-content: center;
    align-items: center;
    text-align: center;
    border-top: 1px rgba(129, 129, 129, 0.322) solid;
    padding: 2px 0 0 0;
    background-color: rgba(88, 110, 98, 0.349);
    user-select: none;
    transition: 0.2s all;
}

.add-story-container:hover {
  background-color: rgba(105, 105, 105, 0.247);
  cursor: pointer;
}

.add-story-container:active {
  background-color: rgba(218, 218, 218, 0.247);
  cursor: pointer;
}

.add-story {
    color: rgb(255, 255, 255);
    font-size: 16px;
    margin: 10px 0px 10px 0px;

}

.main-title-container {
    display: flex;
    margin: 5px 0 5px 0;
    justify-content: center;
    align-items: center;
    text-align: center;

}

.main-title {
    color: bisque;
    font-size: 25px;
    margin: 10px 0px 10px 0px;

}

.story-container {
  border: hsla(0,0%,51%,.322) 1px solid;
  border-radius: 2px 2px 0 0;
  background-color: rgb(43, 43, 46);
}

.story__article {
    padding: 5px 10px 5px 10px;
    border-radius: 10px 10px 0px 0px;
    cursor: pointer;
    transition: all 0s;
    background-color: rgb(46, 46, 53);
    color: rgb(223, 223, 223);

    transition: 0.2s all;
}

.story__article1 {
    padding: 5px 10px 5px 10px;
    border-radius: 0px 0px 0px 0px;
    cursor: pointer;
    transition: all 0s;
    background-color: rgb(43, 43, 46);
    color: rgb(223, 223, 223);

    transition: 0.2s all;
}

.story__article2 {
    padding: 5px 10px 5px 10px;
    border-radius: 0 0 0 0;
    cursor: pointer;
    transition: all 0s;
    background-color: rgb(43, 43, 46);
    color: rgb(223, 223, 223);

    transition: 0.2s all;
}

.story__article1:hover, .story__article2:hover {
  background-color: rgba(105, 105, 105, 0.05);

}

.story__article1:hover {
  background-color: rgba(105, 105, 105, 0.05);

}

.loader-text {
    background-color: whitesmoke;
    color: rgb(0, 0, 0);
    padding: 5px 10px;
    border-radius: 15px;
    font-weight: bold;
}

.loader-container {
    margin: 100px 0 0 0;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.postbutton {
height: 35px;
font-family: inherit;
border: 0px solid #e5e3ff;
color: rgb(0, 255, 98);
cursor: pointer;
font-size: 15px;
width: 80px;
margin: 0px 5px 7px 0;
background-color: #ffffff1e;
border-radius: 4px;
align-self: flex-end;
}

.postbutton:hover {
background-color: #94949425;
}

#comment {
  background-color: #ffffff;
    border: none;
    border-radius: 10px 10px 10px 10px;
    font-size: 14px;
    font-weight: 500;
    outline: none;
    padding: 8px 8px 8px 20px; /* add left padding */
    width: 100%;
    font: inherit;
    color: rgb(0, 0, 0);
    resize: none;
    overflow: auto;
    box-sizing: border-box;
    margin: 0 5px 0px 0;
    height: 100%;
}

#comment:hover {
  background-color: rgb(224, 224, 224);
}

.add-comment-box {
  padding: 1px 0 0 0;
  background-color: rgb(119 119 119 / 19%);
  border-radius: 10px;
  margin: 10px 0 12px 0;
}

.newstory_comment {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: fit-content;
    padding: 5px 0 5px 0;
    display: flex;
    justify-content: left;
    border-radius: 10px;
    align-items: center;
}

.image_box {
    height: max-content;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-self: start;
}

.buttonbox {
  align-self: stretch;
  display: flex;
  }

  .postimage {
    height: 50px;
    border-radius: 100%;
    margin: 0px 8px 0 10px;
    cursor: pointer;
    transition: all 0.1s;
}

.postimage:hover {  
  filter: brightness(85%);
}
</style>
