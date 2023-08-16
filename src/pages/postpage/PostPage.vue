<template>
    <feed-container v-if="!loading">
      <template v-if="!showEnv">
        <info-message></info-message>

        <post-info :data="infoData"></post-info>
        
        <post-section 
          v-for="chapter, index in mountedChapters" 
          :key="chapter._id.$oid" 
          :chapter="chapter" 
          :startExpanded="index === mountedChapters.length - 1">
        </post-section>
        <login-message v-if="!isLoggedIn" :text="'to comment and continue storylines'"></login-message>
        
        <buttonblock-selector :homePage="false" @selected-tab="handleSelectedTab"></buttonblock-selector>

        <transition name="fade" mode="out-in">
          <component :is="selectedTab" :loading="loading" :replies="[]" :chapterList="[]"></component>
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
import LoaderComponent from "@/components/UIcomponents/LoaderComponent.vue";
import DraggableEnvironment from "@/components/UIcomponents/DraggableEnvironment.vue";

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
    PostInfo,
    LoaderComponent,
    DraggableEnvironment
  },
  data() {
    return {
      loading: true,
      mountedChapters: null,
      showEnv: false,
      selectedTab: 'replies-feed',
      infoData: {
        title: "THE QUEST OF CSGO",
        tags: ["chill", "sci-fi", "short"],
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
        this.mountedChapters = response.data.chapters;
        console.log(this.mountedChapters)
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
</style>