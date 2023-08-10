<template>
  <feed-container>
    <section class="section_title">
      Start new story
    </section>
      <div v-if="!loading" class="pollancre">
          <form @submit.prevent="submitForm">
              <div class="newstory_comment">
                  <div class="image_box">
                      <img class="postimage" v-if="userFetchedPicture" :src="imgSource" alt="profilepic">
                  </div>
                  <div class="extended-container">
                    <textarea id="comment" v-model="formcomment" placeholder="Author comment" rows="1" :style="{ height: textareaHeight }" required></textarea>
                  <span class="story__user-name3"><b>@{{ currentUser }}</b> · Now</span>
              </div>
              </div>
              <div class="newstory_title">
                  <input id="title" v-model="formtitle" type="text" placeholder="Story title" required>
              </div>
              <div class="newstory_title">
                  <textarea id="body" v-model="formbody" placeholder="Prologue content" required></textarea>
              </div>
              <div class="tag-section">
                <tags-message></tags-message>
                <div class="tag-list">
                    <post-tag v-for="tag in availableTags" :key="tag" :clickable="isClickable" :reachedMax="reachedMax" :tag="tag" @selected="onSelected"></post-tag>
                </div>

              </div>
              <div class="buttonbox">
                <submit-button :text="'SUBMIT'" :margin="true" :buttonLoading="buttonLoading">
                  <span class="material-symbols-outlined">outgoing_mail</span>
                </submit-button>
              </div>
          </form>
      </div>
      <div v-else class="loader-container">
        <div class="spinner-border spinner-border-sm" style="width: 5rem; height: 5rem;" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
        <span class="loader-text">Planting story seed...</span>
      </div>
  </feed-container>
</template>
  
<script>
import { mapGetters } from 'vuex';
import { API_BASE_URL } from '../config';

import SubmitButton from '@/components/layout/SubmitButton.vue';
import FeedContainer from '@/components/layout/FeedContainer.vue';
import axios from 'axios';
import router from '@/router';
import PostTag from '@/components/layout/PostTag.vue';
import TagsMessage from '@/components/layout/messages/TagsMessage.vue';

export default {
  name: "NewPost",
  components: {
    FeedContainer,
    PostTag,
    SubmitButton,
    TagsMessage
  },
  data() {
    return {
      formtitle: "",
      formcomment: "",
      formbody: "",
      textareaHeight: 0,
      textareaHeight1: 0,
      loading: false,
      buttonLoading: false,
      isPostButtonDisabled: false,
      availableTags: ["sci-fi", "mystery", "chill", "short", "long", "medieval", "jungle", "horror", "historical", "fantasy", "world-building", "romance", "thriller",
                      "young-adults", "humor", "self-help", "action", "suspense", "fairy", "pirate", "space", "science", "contemporary", "spirituality", "politics", "paranormal",
                      "crime", "speculation", "literature", "travel", "development", "adventure", "classic", "detective", "memoir"],
      selectedTags: [],
      isClickable: true,
      reachedMax: false
    };
  },
  methods: {
    onSelected(tag, selected) {
        if (selected) {
          this.selectedTags.push(tag);
        } else {
          this.selectedTags.splice(this.selectedTags.indexOf(tag), 1);
        }
    },
    load() {
      this.buttonLoading = true
      setTimeout(() => {
        this.buttonLoading = false
      }, 3000)
    },
    submitForm() {
      const data_packet = {
        comment: this.formcomment,
        title: this.formtitle,
        body: this.formbody,
        username: this.currentUser,
        tags: this.selectedTags
      }
      this.buttonLoading = true;

      axios
      .post(`${API_BASE_URL}/new_post`, data_packet)
      .then(response => {
          this.buttonLoading = false;
          const data = response.data;
          if (data.status === "Success") {
              router.push("/home")
          }
        })
        .catch(error => {
            console.log(error);
            this.loading = false;
        });
    },
    adjustTextareaHeight() {
        const textarea = this.$el.querySelector('#comment');
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
        this.textareaHeight = textarea.style.height;
      },
      adjustTextareaHeight1() {
        const textarea1 = this.$el.querySelector('#body');
        textarea1.style.height = 'auto';
        textarea1.style.height = textarea1.scrollHeight + 'px';
        this.textareaHeight1 = textarea1.style.height;
      },

  },
  watch: {
      formcomment() {
        this.formcomment = this.formcomment.substring(0, 300);
        this.adjustTextareaHeight();
      },
      formbody() {
        this.formbody = this.formbody.substring(0, 8001);
        this.adjustTextareaHeight1();
      },
      formtitle() {
        this.formtitle = this.formtitle.substring(0, 66);
      }
    },
  mounted() {
    this.adjustTextareaHeight();
  },
  computed: {
    ...mapGetters('auth', ['currentUser', "userFetchedPicture", "colorFetched", "userFetchedBio", "nFetchedPosts", "nFetchedFollowers", "nFetchedFollowing"]),
    imgSource() {
        return require('../assets/img/' + this.userFetchedPicture);
      },
      postButtonText() {
          return this.isPostButtonDisabled ? "Submitted" : "Submit?"
      }
  }
};
</script>

<style scoped>
.tag-section {
  display: flex;
  flex-direction: column;
  justify-content: left;
  margin: 15px 10px 0px 10px;
}

.tag-title {
  color: white;
  margin: 0 0 2px 1px;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;
  margin: 7px 0px 0px 0px;
}

.extended-container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.story__user-name3 {
  color: whitesmoke;
  text-decoration: none;
  margin: 0 4px 0 0;
}

.section_title {
  padding-bottom: 2px;
  margin: 35px 10px 20px 10px;
  font-size: larger;
  font-weight: bold;
  color: rgb(0, 248, 174);
  border-bottom: 2px solid rgb(180, 255, 233);
}

.pollancre {
  padding: 1px 0 0 0;
  background-color: rgb(119 119 119 / 19%);
  border-radius: 4px;
}

.image_box {
  height: max-content;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-self: end;
}

.newstory_comment {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
  margin: 20px 0 10px 0;
  display: flex;
  justify-content: left;
  border-radius: 10px;
}

.postimage {
  height: 55px;
  border-radius: 100%;
  margin: 10px 8px 0 10px;
  border: 0px whitesmoke solid;
}

textarea {
  background-color: #1d252e;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  font-weight: 500;
  outline: none;
  padding: 8px 8px 8px 20px; /* add left padding */
  width: 95%;
  font: inherit;
  outline: rgb(100, 100, 100) 1px solid;
  color: whitesmoke;
  resize: none;
  overflow: auto;
  box-sizing: border-box;
  margin: 0 10px 0 0;
}

#comment {
  background-color: #ffffff;
  border: none;
  border-radius: 10px 10px 10px 0;
  font-size: 14px;
  font-weight: 500;
  outline: none;
  padding: 8px 8px 8px 20px; /* add left padding */
  width: 95%;
  font: inherit;
  color: rgb(0, 0, 0);
  resize: none;
  overflow: auto;
  box-sizing: border-box;
  margin: 0 10px 8px 0;
  transition: 0.2s all;
}

#comment:hover {
  background-color: rgb(224, 224, 224);
}

#body {
  background-color: #1d252e;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  font-weight: 500;
  outline: none;
  padding: 8px 8px 8px 20px; /* add left padding */
  width: 100%;
  font: inherit;
  color: rgb(255, 255, 255);
  resize: none;
  overflow: auto;
  box-sizing: border-box;
  margin: 10px 10px 0px 10px;
  transition: 0.2s all;
}

#body:hover {
  background-color: #161d24;
}

.newstory_title {
  display: flex;
  width: 100%;
}

input[type="text"] {
  background-color: bisque;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  font-weight: 500;
  height: 35px;
  outline: none;
  padding: 8px 8px 8px 20px; /* add left padding */
  width: 100%;
  font: inherit;
  color: rgb(0, 0, 0);
  box-sizing: border-box;
  margin: 0 10px 0 10px;
  transition: 0.2s all;
}
  
input[type="text"]:hover {
    background-color: rgb(214, 193, 167);
}

input[type="text"]::placeholder {
  color: #000000a1;
  font-weight: 400;
}

textarea::-webkit-scrollbar {
    width: 0.5em;
}

textarea::-webkit-scrollbar-track {
  background: transparent;
}

textarea::-webkit-scrollbar-thumb {
  background-color: transparent;
}

.buttonbox {
  display: flex;
  justify-content: flex-end;
  flex-direction: row;
}
</style>