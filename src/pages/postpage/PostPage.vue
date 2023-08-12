<template>
    <feed-container v-if="!loading">
      <info-message></info-message>
      <!--
      <tree-chart :json="data" :class="{landscape: landscape.length}" @click-node="clickNode" class="tree"></tree-chart>
      -->
      <post-info :data="infoData"></post-info>
      <post-section v-for="chapter in chapters" :key="chapter.ide" :chapter="chapter"></post-section>
      <login-message v-if="!isLoggedIn" :text="'to comment and continue storylines'"></login-message>
      
      <buttonblock-selector :homePage="false" @selected-tab="handleSelectedTab"></buttonblock-selector>

      <transition name="fade" mode="out-in">
        <component :is="selectedTab" :loading="loading" :replies="replies" :chapterList="[]"></component>
      </transition>

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
    LoaderComponent
  },
  data() {
    return {
      loading: true,
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