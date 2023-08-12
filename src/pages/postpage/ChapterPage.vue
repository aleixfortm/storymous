<template>
    <feed-container v-if="!loading">
      <info-message></info-message>    
      <div class="story-container">
        <div v-for="chapter in chapterList" :key="chapter._id">
          <template v-if="chapter.type === 'prologue'">
            <div class="main-title-container">
                <h2 class="main-title">{{ chapter.title.toUpperCase() }}</h2>
            </div>
            <div class="tag-section">
                <post-tag v-for="tag in chapter.tags" :key="tag" :clickable="false" :tag="tag"></post-tag>
            </div> 
            <div class="story-stats user-select-none">
              <div class="story-stats-section" 
                    :class="[postData.leaves.includes(currentUser) ? 'includes-leaf-icon' : '']" 
                    @mouseover="showLeavesTooltip = true" 
                    @mouseout="showLeavesTooltip = false">
                <span class="material-symbols-outlined margin1 leaf-icon" :class="[postData.leaves.includes(currentUser) ? 'includes-leaf-icon' : '']">nest_eco_leaf</span>
                <span>{{ totalLeaves }}</span>
                <small-tooltip :condition="showLeavesTooltip" :text="'Storyline leaves'" :top="'35px'"></small-tooltip>
              </div>
              <div class="story-stats-section" @mouseover="showViewsTooltip = true" @mouseout="showViewsTooltip = false">
                <span class="material-symbols-outlined margin1">bar_chart</span>
                <span>{{ highestViews }}</span>
                <small-tooltip :condition="showViewsTooltip" :text="'Highest views'" :top="'35px'"></small-tooltip>
              </div>
              <div class="story-stats-section" @mouseover="showChaptersTooltip = true" @mouseout="showChaptersTooltip = false">
                <span class="material-symbols-outlined margin1">call_split</span>
                <span> {{ chapterList[chapterList.length - 1].chapter_num }} </span>
                <small-tooltip :condition="showChaptersTooltip" :text="'Mounted chapters'" :top="'35px'"></small-tooltip>
              </div>
              <div class="story-stats-section" @mouseover="showCommentsTooltip = true" @mouseout="showCommentsTooltip = false">
                <span class="material-symbols-outlined margin1">chat</span>
                <span>{{ postData.user_comments.length }}</span>
                <small-tooltip :condition="showCommentsTooltip" :text="'Comments'" :top="'35px'"></small-tooltip>
              </div>
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
        <div v-if="isLoggedIn">
          <div class="add-story-container" @click="toggleContinueContainer">
            <h2 class="add-story d-flex align-items-center">CONTINUE STORYLINE <span class="material-symbols-outlined margin-arrow">arrow_forward</span>  <span class="highlight1">CHAPTER</span>
            <span class="highlight1 m-1">{{ chapterList[chapterList.length - 1].chapter_num + 1 }}</span>
            </h2>
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
      </div>   
      </div>

      <login-message v-if="!isLoggedIn" :text="'to comment and continue storylines'"></login-message>
      <div class="add-comment-box" v-else>
        <form @submit.prevent="submitComment">
            <div class="newstory_comment">
                <div class="image_box">
                    <img class="postimage" :src="imgSource" alt="profilepic">
                </div>
                <textarea id="comment" v-model="formcomment" placeholder="Add a comment..." rows="1" :style="{ height: textareaHeight }" required></textarea>
                <div class="buttonbox">
                  <comment-button :text="'COMMENT'" :margin="true">
                    <span class="material-symbols-outlined">chat_bubble</span>
                  </comment-button>
                </div>
            </div>
        </form>
      </div>

      <buttonblock-selector :homePage="false" @selected-tab="handleSelectedTab"></buttonblock-selector>

      <transition name="fade" mode="out-in">
        <component :is="selectedTab" :loading="loading" :replies="replies" :chapterList="chapterList"></component>
      </transition>

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
import { API_BASE_URL } from '../../config';
import { mapGetters } from 'vuex';

import FeedContainer from '@/components/frames/FeedContainer.vue';
import ChapteredContainer from "@/components/postreplies/ChapteredContainer.vue";
import ChapteredprologueContainer from "@/components/postreplies/ChapteredprologueContainer.vue";
import CommentContainer from "@/components/postreplies/CommentContainer.vue";
import ContinuestoryContainer from "@/components/postreplies/ContinuestoryContainer.vue";
import WritechapterContainer from "@/components/postreplies/WritechapterContainer.vue";
import AstronautMessage from "@/components/messages/AstronautMessage.vue";
import PostTag from "@/components/UIcomponents/PostTag.vue";
import CommentButton from "@/components/UIcomponents/buttons/CommentButton.vue";
import SmallTooltip from "@/components/UIcomponents/SmallTooltip.vue";
import InfoMessage from "@/components/messages/InfoMessage.vue";
import LoginMessage from "@/components/messages/LoginMessage.vue";
import RepliesFeed from "./RepliesFeed.vue";
import ChaptersFeed from "./ChaptersFeed.vue";
import CommentsFeed from "./CommentsFeed.vue";
import ButtonblockSelector from "@/components/UIcomponents/ButtonblockSelector.vue";

export default {
  components: {
    FeedContainer,
    ChapteredContainer,
    ChapteredprologueContainer,
    CommentContainer,
    ContinuestoryContainer,
    WritechapterContainer,
    AstronautMessage,
    PostTag,
    CommentButton,
    SmallTooltip,
    InfoMessage,
    LoginMessage,
    RepliesFeed,
    ChaptersFeed,
    CommentsFeed,
    ButtonblockSelector
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
      totalLeaves: 0,
      showLeavesTooltip: false,
      showChaptersTooltip: false,
      showCommentsTooltip: false,
      showViewsTooltip: false,
      highestViews: 0,
      selectedTab: 'replies-feed'
    }
  },
  mounted() {
    const chapterId = this.$route.params.id;
    axios
      .get(`${API_BASE_URL}/chapter/${chapterId}`)
      .then(response => {
        this.chapterList = response.data;
        this.chapterList.forEach((chapter) => {
          if (chapter.views > this.highestViews) {
            this.highestViews = chapter.views;
          }
        });

        this.postData = this.chapterList[0];
        this.totalLeaves += this.postData.leaves.length;

        this.chapterList.forEach((chapter) => {
          this.totalLeaves += chapter.leaves.length;
        });

        this.loading = false;

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
       return require("@/assets/img/" + this.userFetchedPicture);
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
    },
    handleSelectedTab(tab) {
          if (tab === "all") {
            this.selectedTab = "replies-feed";
          } else if (tab === "chapters") {
            this.selectedTab = "chapters-feed"
          } else {
            this.selectedTab = "comments-feed"
          }
            
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
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.1s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0.1;
}

.margin-arrow {
  margin: 0px 4px;
}

.margin-s {
  margin-left: -6px;
}

.highlight1 {
  background-color: bisque;
    color: black;
    border-radius: 2px;
    padding: 0 3px;
}

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 1,
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
    position: relative;
    display: flex;
    align-items: center;
    margin: 0 12px;
    padding: 1px 6px 1px 1px;
    cursor: pointer;
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
    background-color: rgba(85, 85, 85, 0.753);
    user-select: none;
    transition: 0.2s all;
}

.add-story-container:hover {
  background-color: rgba(122, 122, 122, 0.247);
  cursor: pointer;
}

.add-story-container:active {
  background-color: rgba(218, 218, 218, 0.247);
  cursor: pointer;
}

.add-story {
    color: rgb(255, 255, 255);
    font-size: 16px;
    font-weight: bold;
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
  justify-content: center;
  align-items: center;
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
