<template>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,300,1,200" />
    <feed-container v-if="!loading">
      <disclaimer-message></disclaimer-message>
      <div class="story-container">
        <div class="main-title-container">
          <h2 class="main-title">{{ post.title.toUpperCase() }}</h2>
        </div>
        <div class="tag-section">
            <post-tag v-for="tag in post.tags" :key="tag" :clickable="false" :tag="tag"></post-tag>
        </div> 
        <div class="story-stats">
            <div class="story-stats-section">
              <span class="material-symbols-outlined margin1 leaf-icon" 
                    :class="[post.leaves.includes(currentUser) ? 'includes-leaf-icon' : '']"
                    >nest_eco_leaf
                  </span>
                  {{ post.leaves.length }}
              </div>
            <div class="story-stats-section"><span class="material-symbols-outlined margin1">bar_chart</span>{{ post.views }}</div>
            <div class="story-stats-section"><span class="material-symbols-outlined margin1">chat</span>{{ post.user_comments.length }}</div>
            <div class="story-stats-section"><span class="material-symbols-outlined margin1">share</span></div>
        </div>

        <chapteredprologue-container
          v-if="post"
            :_id="post._id"
            :title="post.title"
            :content="post.content"
            :username="post.username"
            :postComment="post.comment"
            :date="post.date"
            :picture="post.picture"
            :color="post.color"
            :feedMode="false"
            class="story__article">
        </chapteredprologue-container>
        <span v-if="isLoggedIn">
          <div class="add-story-container" @click="toggleContinueContainer">
            <h2 class="add-story"> WRITE CHAPTER 1 (START NEW STORYLINE)</h2>
          </div>
          <writechapter-container
          v-if="showContinueContainer"
          :chapterNum="1"
          :username="currentUser"
          :postId="post._id"
          :postTitle="post.title"
          :parentChapterId="null">
        </writechapter-container>
        </span>   
      </div>
      <div class="pollancre" v-if="isLoggedIn">
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
      <div v-if="!isLoggedIn" class="alert alert-info mt-2 shadow p-2" role="alert">
        <b>Log in</b> to write comments and continue storylines
      </div>
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
        <template v-else>
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
      <astronaut-message v-if="replies.length == 0" 
        :onomatopoeia="'crick crick'" 
        :text="'No comments or chapters have been written for this story yet. You can be the first, hurry up!'">
      </astronaut-message>
    </feed-container>
    <feed-container v-else>
      <div class="loader-container">
        <div class="spinner-border text-light mb-3" style="width: 5rem; height: 5rem;" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
          <span class="loader-text">Harvesting story from story tree</span>
      </div>
    </feed-container>
</template>

<script>
import axios from "axios";
import { API_BASE_URL } from '../config';
import { mapGetters } from 'vuex';

import CommentContainer from "@/components/layout/CommentContainer.vue";
import ContinuestoryContainer from "../components/layout/ContinuestoryContainer.vue";
import FeedContainer from '@/components/layout/FeedContainer.vue';
import ChapteredprologueContainer from "@/components/layout/ChapteredprologueContainer.vue";
import WritechapterContainer from "@/components/layout/WritechapterContainer.vue";
import AstronautMessage from "@/components/layout/messages/AstronautMessage.vue";
import DisclaimerMessage from "@/components/layout/messages/DisclaimerMessage.vue";
import PostTag from "@/components/layout/PostTag.vue";

export default {
  components: {
    FeedContainer,
    AstronautMessage,
    CommentContainer,
    ContinuestoryContainer,
    ChapteredprologueContainer,
    WritechapterContainer,
    DisclaimerMessage,
    PostTag
  },
  data() {
    return {
      post: null,
      replies: null,
      formcomment: "",
      continuedStory: null,
      textareaHeight: null,
      loading: true,
      showContinueContainer: false
    }
  },
  mounted() {
    const postId = this.$route.params.id;
    axios
      .get(`${API_BASE_URL}/post/${postId}`)
      .then(response => {
        this.post = response.data.post;
        this.replies = response.data.replies;
        this.loading = false;
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
            parentId: this.post._id.$oid,
          }

          axios
            .post(`${API_BASE_URL}/new_comment`, data_packet)
            .then(response => {
              const dataPayload = response.data;
              //const comment_data = dataPayload.data_payload;

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
    margin: 5px 0 2px 5px;
    justify-content: center;
}

.story-stats-section {
    display: flex;
    align-items: center;
    margin-right: 25px;
    padding: 1px 6px 1px 1px;
}

.story-stats-section:hover {
    background-color: rgba(194, 194, 194, 0.137);
    border-radius: 10px;
}

.story__article {
    padding: 5px 10px 5px 10px;
    border-radius: 0px 0px 0px 0px;
    cursor: pointer;
    transition: all 0s;
    background-color: rgb(43, 43, 46);
    color: rgb(223, 223, 223);

    transition: 0.2s all;
}

.story__article:hover {
    background-color: rgba(105, 105, 105, 0.041);

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

.add-story-container {
    display: flex;
    margin: 5px 0 5px 0;
    justify-content: center;
    align-items: center;
    text-align: center;
    border-top: 1px rgba(129, 129, 129, 0.322) solid;
    padding: 2px 0 0 0;
    background-color: rgba(86, 175, 123, 0.349);
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

.border-top {
  border-top: solid 1px rgba(129, 129, 129, 0.322) 1px solid;
}


.story-container {
  border: hsla(0,0%,51%,.322) 1px solid;
  border-radius: 2px 2px 0 0;
  background-color: rgb(43, 43, 46);
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

.pollancre {
  padding: 1px 0 0 0;
  background-color: rgb(119 119 119 / 19%);
  border-radius: 10px;
  margin: 5px 0 12px 0;
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
