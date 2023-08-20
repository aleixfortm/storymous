<template>
    <div @click="redirectToChapter" class="userdata">
        <div class="whote-data-container">
            <div class="name-container">
                <div class="title">{{ story.title }}</div>
            </div>
            <div class="stats-data-container">
              
              <div class="data-value">
                   <span class="material-symbols-outlined custom-i">bar_chart</span>
                  <div class="views-num">{{ story.views }}</div>
              </div>
              <img class="userimg" v-if="story.picture" :src="imgSource" alt="astronaut">
              <img class="userimg" v-else src="@/assets/img/moon_default_avatar-min.png" alt="default avatar">
              <div class="username">
                 @{{ story.username }}
              </div>
            </div>
        </div>  
    </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
    props: ["story"],
    setup() {
        const router = useRouter();
        return { router: router };
    },
    computed: {
        imgSource() {
            return require("@/assets/img/" + this.story.picture)
        }
    },
    methods: {
      redirectToChapter() {
        this.router.push(`/chapter/${this.story._id.$oid}`);
      }
    }
}
</script>

<style scoped>
.username {
  color: rgb(255, 255, 255);
  font-weight: bold;
  font-size: 13px;
  margin: 0 0 0 3px;
}
.views-num {
  margin: 2px 0 0 -2px;
  color: white;
}
.custom-i {
    font-size: 22px;
  height: fit-content;
  font-variation-settings:
  'FILL' 1,
  'wght' 200,
  'GRAD' -25,
  'opsz' 0
}
.stats-data-container {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin: 0 0 0 0px;
}
.data-value {
  display: flex;
  justify-content: left;
  align-items: left;
  margin: 0 15px 0 0;
}
.title:hover {
  text-decoration: underline;
}
.userdata:hover {
  background-color: #adadad1e;
}
.title {
  height: fit-content;
  margin: 0 5px 0 5px;
  color: rgb(255, 222, 185);
  font-weight: bold;
}
.name-container {
  display: flex;
  flex-direction: column;
  width: fit-content;
  margin: 0;
}
.whote-data-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin: 0;
}
.userimg {
  height: 18px;
  width: auto;
  border-radius: 100%;
}

.userdata {
  display: flex;
  padding: 4px 0px 4px 4px;
  font-family: inherit;
  color: rgb(107, 154, 255);
  cursor: pointer;
  font-size: 15px;
  width: fit-content;
  justify-content: flex-start;
  background-color: #ffffff09;
  width: 100%;
  border-radius: 4px;
  align-items: center;
  margin: 8px 0 0 0;
  transition: all 0.2s;
}
</style>