<template>
    <feed-container v-if="!loading">
      <template v-if="!showEnv">
        <info-message></info-message>

        <post-info :data="infoData"></post-info>

        <TransitionGroup name="list" tag="ul">
          <post-section 
            v-for="chapter, index in mountedChapters" 
            :key="chapter._id.$oid" 
            :chapter="chapter" 
            :startExpanded="index === mountedChapters.length - 1">
          </post-section>
        </TransitionGroup>

        <div class="buttons-container">
          <unmount-button v-if="mountedChapters.length > 1" @click="unmountChapter" :text="unmountButtonText" class="unmount-button"></unmount-button>
        </div>

        <login-message v-if="!isLoggedIn" :text="'to add comments and continue storylines'"></login-message>
        
        <buttonblock-selector :homePage="false" @selected-tab="handleSelectedTab"></buttonblock-selector>

        <transition name="fade" mode="out-in">
          <component :is="selectedTab" :loading="loading" :comments="comments" :chapters="mountableChapters" @selected-chapter="handleSelectedChapter"></component>
        </transition>
      </template>
      <template v-else>
        <draggable-environment>
          <tree-chart :json="treeData" :class="{landscape: landscape.length}" @click-node="clickNode" class="tree"></tree-chart>
        </draggable-environment>
      </template>
    </feed-container>
    <feed-container v-else>
      <loader-component :text="'Harvesting story from story tree'"></loader-component>
    </feed-container>
</template>

<script>
import axios from "axios";
import { API_BASE_URL } from '../../config';
import { mapGetters } from 'vuex';

import PostSection from "./PostSection.vue";
import FeedContainer from '@/components/frames/FeedContainer.vue';
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
import LoaderComponent from "@/components/UIcomponents/LoaderComponent.vue";
import DraggableEnvironment from "@/components/UIcomponents/DraggableEnvironment.vue";
import UnmountButton from "@/components/UIcomponents/buttons/UnmountButton.vue";

export default {
  components: {
    FeedContainer,
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
    PostInfo,
    LoaderComponent,
    DraggableEnvironment,
    UnmountButton
  },
  data() {
    return {
      loading: true,
      loadingReplies: true,
      mountedChapters: [],
      mountableChapters: [],
      chapters: [],
      comments: [],
      showEnv: false,
      selectedTab: 'comments-feed',
      infoData: {
        title: "THE QUEST OF CSGO",
        tags: ["chill"],
        leaves: ["stoupeaks", "benetti"],
        views: 230,
        user_comments: []
      },
      landscape: [],
      treeData: {
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
          },
          {
              name: 'Chapter 1',
              image_url: require("@/assets/img/astronaut_reading.jpeg")
          },
          {
              name: 'Chapter 1',
              image_url: require("@/assets/img/astronaut_reading.jpeg")
          },
          {
              name: 'Chapter 1',
              image_url: require("@/assets/img/astronaut_reading.jpeg")
          },
          ]
      },
    }
  },
  mounted() {
    const chapterId = this.$route.params.id;
    axios
      .get(`${API_BASE_URL}/chapter/${chapterId}`)
      .then(response => {
        this.mountedChapters = response.data.mountedChapters;
        this.chapters = response.data.allChapters;
        this.comments = response.data.comments;
        this.loadingReplies = false;
        this.loading = false;

        // make mountableChapters be all those that its parent_id equal to the id of the last mountedChapter object
        const lastChapterId = this.mountedChapters[this.mountedChapters.length - 1]._id.$oid;
        this.mountableChapters = this.chapters.filter(chapter => chapter.parent_id.$oid === lastChapterId);
    })
  },
  computed: {
    ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched"]),
    imgSource() {
       return require("@/assets/img/" + this.userFetchedPicture);
    },
    unmountButtonText() {
      return "Unmount"
      //return "Unmount chapter " + (this.mountedChapters.length - 1)
    }
  },
  methods: {
    handleSelectedTab(tab) {
      if (tab === "chapters") {
        this.selectedTab = "chapters-feed"
      } else {
        this.selectedTab = "comments-feed"
      }           
    },
    handleSelectedChapter(data) {
      // find chapter in chapters that contains the emitted _id
      const foundChapter = this.chapters.find(chapter => chapter._id === data);
      if (foundChapter) {
        this.mountedChapters.push(foundChapter)
        const lastChapterId = this.mountedChapters[this.mountedChapters.length - 1]._id.$oid;
        this.mountableChapters = this.chapters.filter(chapter => chapter.parent_id.$oid === lastChapterId);
      } else {
        console.log("Chapter not found");
      }
    },
    unmountChapter() {
      if (this.mountedChapters.length > 1){
        this.mountedChapters.pop()
        const lastChapterId = this.mountedChapters[this.mountedChapters.length - 1]._id.$oid;
        this.mountableChapters = this.chapters.filter(chapter => chapter.parent_id.$oid === lastChapterId);
      }
      
    }
  },
}
</script>

<style scoped>
.buttons-container {
  display: flex;
  justify-content: flex-end;
}

.unmount-button {
  margin: 5px 0 0 0;
}

ul {
  padding: 0;
  margin: 0;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.4s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

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

@media (max-width: 700px) {
  .unmount-button {
    margin: 5px 5px 0 0;
  }
}
</style>