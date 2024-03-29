<template>
    <feed-container v-if="!loading">
      <template v-if="!showEnv">
        <info-message></info-message>

        <post-info :data="storylineData"></post-info>

        <TransitionGroup name="list" tag="ul">
          <post-section 
            v-for="chapter, index in mountedChapters" 
            :key="chapter._id.$oid" 
            :chapter="chapter" 
            :startExpanded="index === mountedChapters.length - 1">
          </post-section>
        </TransitionGroup>

        <div class="buttons-container">
          <writechapter-button v-if="!isSelectedWriteChapter" @click="writeChapter" :text="'Write chapter'" class="mount-button buttons-group-1">
            <span class="material-symbols-outlined small-font">edit</span>
          </writechapter-button>
          <div v-if="!isSelectedWriteChapter" class="buttons-group-2">
            <mount-button :disabledButton="mountableChapters.length > 0" @click="mountRandomChapter" :text="mountButtonText" class="mount-button">
              <span class="material-symbols-outlined small-font">shuffle</span>
            </mount-button>
            <unmount-button :disabledButton="mountedChapters.length > 1" @click="unmountChapter" :text="unmountButtonText" class="unmount-button">
              <span class="material-symbols-outlined small-font">switch_access_shortcut</span>
            </unmount-button>
          </div>
        </div>
        <writechapter-container
          v-if="isSelectedWriteChapter && isLoggedIn"
          :last_chapter="mountedChapters[mountedChapters.length - 1]"
          @written-chapter="handleWrittenChapter"
        >
          <div class="close-container"><span @click="writeChapter" class="material-symbols-outlined bigger-font">close</span></div>
        </writechapter-container>
        <login-message v-if="!isLoggedIn" :text="'to add comments and continue storylines'"></login-message>
        
        <buttonblock-selector :homePage="false" @selected-tab="handleSelectedTab"></buttonblock-selector>

        <transition name="fade" mode="out-in">
          <component :is="selectedTab" :loading="loading" :comments="comments" :chapters="mountableChapters" :story_id="mountedChapters[0].story_id" @selected-chapter="handleSelectedChapter"></component>
        </transition>
      </template>
      <template v-else>
        <draggable-environment>
          <tree-chart :json="treeData" :class="{landscape: landscape.length}" @click-node="clickNode" class="tree"></tree-chart>
        </draggable-environment>
      </template>
    </feed-container>
    <feed-container v-else>
      <loader-component :text="'Mounting chapters to story'"></loader-component>
    </feed-container>
</template>

<script>
import axios from "axios";
import { API_BASE_URL } from '../../config';
import { mapGetters } from 'vuex';
import { mapActions } from "vuex";

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
import MountButton from "@/components/UIcomponents/buttons/MountButton.vue";
import WritechapterButton from "@/components/UIcomponents/buttons/WritechapterButton.vue";

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
    UnmountButton,
    MountButton,
    WritechapterButton,
  },
  data() {
    return {
      loading: true,
      loadingReplies: true,
      mountedChapters: [],
      mountableChapters: [],
      chapters: [],
      comments: [],
      isSelectedWriteChapter: false,
      showEnv: false,
      selectedTab: 'comments-feed',
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
    window.scrollTo(0, 0);
    const chapterId = this.$route.params.id;
    axios
      .get(`${API_BASE_URL}/chapter/${chapterId}`)
      .then(response => {
        this.mountedChapters = response.data.mountedChapters;
        this.chapters = response.data.allChapters;
        this.comments = response.data.comments;
        this.setContributors(response.data.contributors)
        this.setNewStatus(true)
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
    mountButtonText() {
      return "Mount random"
    },
    unmountButtonText() {
      return "Unmount last"
    },
    storylineData() {
      const chapterWithHighestViews = this.mountedChapters.reduce((maxChapter, chapter) => {
        if (chapter.views > maxChapter.views) {
          return chapter;
        }
        return maxChapter;
      }, this.mountedChapters[0]);

      const storyData = {
        title: this.mountedChapters[0].title,
        tags: this.mountedChapters[0].tags,
        leaves: this.mountedChapters.reduce((sum, chapter) => sum + chapter.leaves, 0),
        views: chapterWithHighestViews.views,
        user_comments: this.comments,
        mountedChapters: this.mountableChapters.length
      };
      return storyData
    }
  },
  methods: {
    ...mapActions('message', ['setLoginError']),
    ...mapActions('chapterData', ['setContributors', 'setNewStatus']),
    handleSelectedTab(tab) {
      if (tab === "chapters") {
        this.selectedTab = "chapters-feed"
      } else {
        this.selectedTab = "comments-feed"
      }           
    },
    handleWrittenChapter(data) {
      this.mountedChapters.push(data)
      this.chapters.push(data)
      this.isSelectedWriteChapter = false
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
    writeChapter() {
      if (this.isLoggedIn) {
        this.isSelectedWriteChapter = !this.isSelectedWriteChapter
      } else {
        this.setLoginError()
      }
    },
    mountRandomChapter() {
      if (this.mountableChapters.length > 0) {
        const randomIndex = Math.floor(Math.random() * this.mountableChapters.length);
        const randomChapter = this.mountableChapters[randomIndex];
        // Use the randomly selected chapter as needed
        this.handleSelectedChapter(randomChapter._id)
      } else {
        console.log("No mountable chapters available.");
      }
    },
    unmountChapter() {
      if (this.mountedChapters.length > 1) {
        this.mountedChapters.pop()
        const lastChapterId = this.mountedChapters[this.mountedChapters.length - 1]._id.$oid;
        this.mountableChapters = this.chapters.filter(chapter => chapter.parent_id.$oid === lastChapterId);
      }
      
    }
  },
}
</script>

<style scoped>
feed-container {
  position: relative;
}

.bigger-font {
  font-size: 30px;
  cursor: pointer;
}

.bigger-font:hover {
  color: rgba(255, 255, 255, 0.849);
}

.close-container {
  display: flex;
  width: 100%;
  justify-content: flex-end;
  margin: 0 auto -6px auto;
  padding: 2px 5px 0 5px;
  color: rgba(255, 255, 255, 0.562);
}

.buttons-group-1 {
  order: 1;
}

.buttons-group-2 {
  display: flex;
  order: 2;
}

.small-font {
  font-size: 20px;
}

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 500,
  'GRAD' -25,
  'opsz' 0
}

.buttons-container {
  display: flex;
  justify-content: space-between;
  margin: 5px 0px 5px 0px;
}

.mount-button {
  margin: 0 5px 0 0;
}
.unmount-button {
  margin: 0px 0 0 0;
}

ul {
  padding: 0;
  margin: 0;
}

.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.4s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */

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