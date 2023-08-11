<template>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,300,1,200" />
    
    <feed-container v-if="!loading">
      <tree-container></tree-container>
      <info-message></info-message>
      
      <div class="story-container">
        <div class="main-title-container">
          <h2 class="main-title">{{ post.title.toUpperCase() }}</h2>
        </div>
        <div class="tag-section">
            <post-tag v-for="tag in post.tags" :key="tag" :clickable="false" :tag="tag"></post-tag>
        </div> 
        <div class="story-stats user-select-none">
            <div class="story-stats-section" 
                  :class="[post.leaves.includes(currentUser) ? 'includes-leaf-icon' : '']" 
                  @mouseover="showLeavesTooltip = true" 
                  @mouseout="showLeavesTooltip = false">
              <span class="material-symbols-outlined margin1 leaf-icon" :class="[post.leaves.includes(currentUser) ? 'includes-leaf-icon' : '']">nest_eco_leaf</span>
              <span>{{ post.leaves.length }}</span>
              <small-tooltip :condition="showLeavesTooltip" :text="'Storyline leaves'" :top="'35px'"></small-tooltip>
            </div>
            <div class="story-stats-section" @mouseover="showViewsTooltip = true" @mouseout="showViewsTooltip = false">
              <span class="material-symbols-outlined margin1">bar_chart</span>
              <span>{{ post.views }}</span>
              <small-tooltip :condition="showViewsTooltip" :text="'Highest views'" :top="'35px'"></small-tooltip>
            </div>
            <div class="story-stats-section" @mouseover="showChaptersTooltip = true" @mouseout="showChaptersTooltip = false">
              <span class="material-symbols-outlined margin1">call_split</span>
              <span>0</span>
              <small-tooltip :condition="showChaptersTooltip" :text="'Mounted chapters'" :top="'35px'"></small-tooltip>
            </div>
            <div class="story-stats-section" @mouseover="showCommentsTooltip = true" @mouseout="showCommentsTooltip = false">
              <span class="material-symbols-outlined margin1">chat</span>
              <span>{{ post.user_comments.length }}</span>
              <small-tooltip :condition="showCommentsTooltip" :text="'Comments'" :top="'35px'"></small-tooltip>
            </div>
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
            <h2 class="add-story d-flex align-items-center">
              START NEW STORYLINE <span class="material-symbols-outlined margin-arrow">arrow_forward</span> 
              <span class="highlight1 m-1">CHAPTER</span>
              <span class="highlight1">1</span>
            </h2>
          </div>
          <writechapter-container
          v-if="showContinueContainer"
          :chapterNum="1"
          :username="currentUser"
          :postId="post._id"
          :postTitle="post.title"
          :parentChapterId="null"
          :tags="post.tags">
        </writechapter-container>
        </span>   
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
        <component :is="selectedTab" :loading="loading" :replies="replies" :chapterList="[]"></component>
      </transition>

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

import FeedContainer from '@/components/layout/FeedContainer.vue';
import ChapteredprologueContainer from "@/components/layout/ChapteredprologueContainer.vue";
import WritechapterContainer from "@/components/layout/WritechapterContainer.vue";
import PostTag from "@/components/layout/PostTag.vue";
import SmallTooltip from "@/components/layout/SmallTooltip.vue";
import CommentButton from "@/components/layout/CommentButton.vue";
import InfoMessage from "@/components/layout/messages/InfoMessage.vue";
import LoginMessage from "@/components/layout/messages/LoginMessage.vue";
import ButtonblockSelector from "@/components/layout/ButtonblockSelector.vue";
import RepliesFeed from "./subpages/RepliesFeed.vue";
import ChaptersFeed from "./subpages/ChaptersFeed.vue";
import CommentsFeed from "./subpages/CommentsFeed.vue";
import TreeContainer from "@/components/layout/TreeContainer.vue";

export default {
  components: {
    FeedContainer,
    ChapteredprologueContainer,
    WritechapterContainer,
    PostTag,
    SmallTooltip,
    CommentButton,
    InfoMessage,
    LoginMessage,
    ButtonblockSelector,
    RepliesFeed,
    ChaptersFeed,
    CommentsFeed,
    TreeContainer
  },
  data() {
    return {
      post: null,
      replies: null,
      formcomment: "",
      continuedStory: null,
      textareaHeight: null,
      loading: true,
      showContinueContainer: false,
      addedChapters: 0,
      showLeavesTooltip: false,
      showViewsTooltip: false,
      showChaptersTooltip: false,
      showCommentsTooltip:false,
      selectedTab: 'replies-feed',
    }
  },
  mounted() {
    const postId = this.$route.params.id;
    axios
      .get(`${API_BASE_URL}/post/${postId}`)
      .then(response => {
        this.post = response.data.post;
        this.replies = response.data.replies;
        this.replies.forEach(reply => {
          if (reply.type !== "comment") {
            this.addedChapters += 1
          }
        })
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
              this.replies.unshift(dataPayload.comment_data);
              this.formcomment = '';
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
    color: rgb(0, 255, 106);
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
</style>
