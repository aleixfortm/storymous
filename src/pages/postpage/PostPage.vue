<template>
    <feed-container v-if="!loading">
      <info-message></info-message>
      <!--
      <tree-chart :json="data" :class="{landscape: landscape.length}" @click-node="clickNode" class="tree"></tree-chart>
      -->
      <post-info :data="infoData"></post-info>
      <post-section v-for="chapter in chapters" :key="chapter.ide" :chapter="chapter"></post-section>
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
import { API_BASE_URL } from '../../config';
import { mapGetters } from 'vuex';

import PostSection from "./PostSection.vue";
import FeedContainer from '@/components/frames/FeedContainer.vue';
import ChapteredprologueContainer from "./ChapteredprologueContainer.vue";
import WritechapterContainer from "@/components/postreplies/WritechapterContainer.vue";
import PostTag from "@/components/UIcomponents/PostTag.vue";
import SmallTooltip from "@/components/UIcomponents/SmallTooltip.vue";
import CommentButton from "@/components/UIcomponents/buttons/CommentButton.vue";
import InfoMessage from "@/components/messages/InfoMessage.vue";
import LoginMessage from "@/components/messages/LoginMessage.vue";
import ButtonblockSelector from "@/components/UIcomponents/ButtonblockSelector.vue";
import RepliesFeed from "./RepliesFeed.vue";
import ChaptersFeed from "./ChaptersFeed.vue";
import CommentsFeed from "./CommentsFeed.vue";
import TreeChart from "@/components/TreeChart.vue";
import PostInfo from "./PostInfo.vue";

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
    TreeChart,
    PostSection,
    PostInfo
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
      infoData: {
        title: "THE QUEST OF CSGO",
        tags: ["chill", "sci-fi", "short"],
        leaves: ["stoupeaks", "benetti"],
        views: 230,
        user_comments: []
      },
      landscape: [],
      data: {
          name: '@benetti Prologue',
          image_url: require("@/assets/img/astronaut_saloon.jpeg"),
          class: ["rootNode"],
          children: [
          {
              name: 'Chapter 1',
              image_url: require("@/assets/img/astronaut_reading.jpeg")
          },
          {
              name: 'Chapter 1',
              image_url: require("@/assets/img/astronaut_saloon.jpeg"),
              children: [
              {
                  name: 'Chapter 2',
                  image_url: require("@/assets/img/astronaut_saloon.jpeg"),
                  children: [
                      {
                          name: 'Chapter 3',
                          image_url: require("@/assets/img/astronaut_saloon.jpeg"),
                          children: [
                  {
                  name: 'Chapter 4',
                  image_url: require("@/assets/img/astronaut_saloon.jpeg"),
                  children: [
                    {
                        name: 'Chapter 5',
                        image_url: require("@/assets/img/astronaut_saloon.jpeg"),
                        
                    },
                  ]
              },
            ]
                      },
                  ]
              },
              ]
          }
          ]
      },
      chapters: [ 
          {
              isExpandedInfo: false,
              ide: 123,
              type: "prologue",
              title: "Title",
              content: "Content sdfsdafdsa dsf dsafdsa dasf dsfdas fdsf dsf dsaf dsafdsa fdsaf dsa fdsf ds dsfds fds sd fdsf dsf dsfds fds fds fdsfdsfsdafsdf dsf dsfds ds fdsf dsf dsfdsf sdfdsf dsf dsfdsfdsaf dsfds fdsfdsfsdfds fsdf sdfdsfds fd",
              username: "stoupeaks",
              postComment: "This is a big project",
              date: "2 days ago",
              picture: "astronaut_reading.jpeg",
          },
          {
              isExpandedInfo: false,
              ide: 1234,
              type: "chapter",
              title: "Title 2 HAHAHA",
              content: "Content sdfsdafdsa dsf dsafdsa dasf dsfdas fdsf dsf dsaf dsafdsa fdsaf dsa fdsf ds dsfds fds sd fdsf dsf dsfds fds fds fdsfdsfsdafsdf dsf dsfds ds fdsf dsf dsfdsf sdfdsf dsf dsfdsfdsaf dsfds fdsfdsfsdfds fsdf sdfdsfds fd DSFD SAFDS FSAD DS FDSF SDAF DS FSDF DS FDSAF DSF SDAF S",
              username: "benetti",
              postComment: "This is a big project",
              date: "Now",
              picture: "astronaut_saloon.jpeg",
              color: "blue",
              feedMode: false
          },
          {
              isExpandedInfo: false,
              ide: 1234,
              type: "chapter",
              title: "Title 2 HAHAHA",
              content: "Content sdfsdafdsa dsf dsafdsa dasf dsfdas fdsf dsf dsaf dsafdsa fdsaf dsa fdsf ds dsfds fds sd fdsf dsf dsfds fds fds fdsfdsfsdafsdf dsf dsfds ds fdsf dsf dsfdsf sdfdsf dsf dsfdsfdsaf dsfds fdsfdsfsdfds fsdf sdfdsfds fd DSFD SAFDS FSAD DS FDSF SDAF DS FSDF DS FDSAF DSF SDAF S",
              username: "benetti",
              postComment: "This is a big project",
              date: "Now",
              picture: "astronaut_saloon.jpeg",
              color: "blue",
              feedMode: false
          },
          {
              isExpandedInfo: false,
              ide: 1234,
              type: "chapter",
              title: "Title 2 HAHAHA",
              content: "Content sdfsdafdsa dsf dsafdsa dasf dsfdas fdsf dsf dsaf dsafdsa fdsaf dsa fdsf ds dsfds fds sd fdsf dsf dsfds fds fds fdsfdsfsdafsdf dsf dsfds ds fdsf dsf dsfdsf sdfdsf dsf dsfdsfdsaf dsfds fdsfdsfsdfds fsdf sdfdsfds fd DSFD SAFDS FSAD DS FDSF SDAF DS FSDF DS FDSAF DSF SDAF S",
              username: "benetti",
              postComment: "This is a big project",
              date: "Now",
              picture: "astronaut_saloon.jpeg",
              color: "blue",
              feedMode: false
          },
          {
              isExpandedInfo: false,
              ide: 1234,
              type: "chapter",
              title: "Title 2 HAHAHA",
              content: "Content sdfsdafdsa dsf dsafdsa dasf dsfdas fdsf dsf dsaf dsafdsa fdsaf dsa fdsf ds dsfds fds sd fdsf dsf dsfds fds fds fdsfdsfsdafsdf dsf dsfds ds fdsf dsf dsfdsf sdfdsf dsf dsfdsfdsaf dsfds fdsfdsfsdfds fsdf sdfdsfds fd DSFD SAFDS FSAD DS FDSF SDAF DS FSDF DS FDSAF DSF SDAF S",
              username: "benetti",
              postComment: "This is a big project",
              date: "Now",
              picture: "astronaut_saloon.jpeg",
              color: "blue",
              feedMode: false
          },
          {
              isExpandedInfo: false,
              ide: 1234,
              type: "chapter",
              title: "Title 2 HAHAHA",
              content: "Content sdfsdafdsa dsf dsafdsa dasf dsfdas fdsf dsf dsaf dsafdsa fdsaf dsa fdsf ds dsfds fds sd fdsf dsf dsfds fds fds fdsfdsfsdafsdf dsf dsfds ds fdsf dsf dsfdsf sdfdsf dsf dsfdsfdsaf dsfds fdsfdsfsdfds fsdf sdfdsfds fd DSFD SAFDS FSAD DS FDSF SDAF DS FSDF DS FDSAF DSF SDAF S",
              username: "benetti",
              postComment: "This is a big project",
              date: "Now",
              picture: "astronaut_saloon.jpeg",
              color: "blue",
              feedMode: false
          }
      ]
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
       return require("@/assets/img/" + this.userFetchedPicture);
    },
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
.tree {
  margin-top: 25px;
}


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
