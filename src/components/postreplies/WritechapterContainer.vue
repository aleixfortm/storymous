<template>
    <div class="write-container">
        <slot></slot>
        <form @submit.prevent="submitForm">
            <continuechapter-message></continuechapter-message>
            <div class="newstory_comment">
                <div class="image_box">
                    <img class="postimage" v-if="userFetchedPicture" :src="imgSource" alt="profilepic">
                </div>
                <div class="extended-container">
                    <textarea id="comment" v-model="formcomment" placeholder="Author comment e.g. My first chapter!" rows="1" :style="{ height: textareaHeight }" required></textarea>
                    <span class="story__user-name3"><b>@{{ currentUser }}</b> · Now</span>
                </div>
            </div>
            <div class="chapternum">
              <h2 class="story__title ">
                <span class="story_title highlight">CHAPTER</span><span class="story_title highlight margin-minus">{{ last_chapter.chapter_num + 1 }}</span>
              </h2>
            </div>
            <div class="newstory_title marginated">
              <input id="title" class="title-for-story" v-model="formtitle" type="text" placeholder="Chapter name e.g. The lost island" required>
            </div>
            <div class="newstory_title">
                <textarea id="body" v-model="formbody" placeholder="Chapter content" required></textarea>
            </div>
            <div class="buttonbox">
              <submit-button :text="'Submit'" :buttonLoading="loading" :margin="true">
                <span class="material-symbols-outlined">outgoing_mail</span>
              </submit-button>
            </div>
        </form>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import axios, { API_BASE_URL } from '../../config';
import SubmitButton from '../UIcomponents/buttons/SubmitButton.vue';
import ContinuechapterMessage from '../messages/ContinuechapterMessage.vue';

  export default {
    components: {
      SubmitButton,
      ContinuechapterMessage
    },
    props: ["last_chapter"],
    data() {
      return {
        formtitle: "",
        formcomment: "",
        formbody: "",
        textareaHeight: 0,
        textareaHeight1: 0,
        loading: false,
        isPostButtonDisabled: false,
      };
    },
    methods: {
      submitForm() {
        this.loading = true;

        const data_packet = {
          comment: this.formcomment,
          title: this.formtitle,
          content: this.formbody,
          username: this.currentUser,
          story_id: this.last_chapter.story_id.$oid,
          chapter_num: this.last_chapter.chapter_num + 1,
          parent_id: this.last_chapter._id.$oid,
          tags: this.last_chapter.tags
        }

        axios.post(`${API_BASE_URL}/new_chapter`, data_packet)
        .then(response => {
            this.loading = false;
            const data = response.data;
            if (data.status === "Success") {
              data.chapter.picture = this.userFetchedPicture;
              data.chapter.created_at = "Now"
              this.$emit('written-chapter', data.chapter);
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
          return require('@/assets/img/' + this.userFetchedPicture);
        },
        postButtonText() {
            return this.isPostButtonDisabled ? "Submitted" : "Submit?"
        }
    }
  };

</script>

<style scoped>
.margin-minus {
  margin-left: -7px;
}

.infomessage {
  margin: 10px;
}

.chapternum {
  margin: 2px 0 5px 10px;
}

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 500,
  'GRAD' -25,
  'opsz' 0;
  font-size: 20px;
}
.story__user-name3 {
    color: whitesmoke;
    text-decoration: none;
    margin: 0 4px 0 0;
}

.extended-container {
    display: flex;
    flex-direction: column;
    width: 100%;
}


.story__title {
    color: bisque;
    font-size: 17px;
    align-self: center;
    justify-self: center;
    margin: 0px 0px 0px 0px;
    font-weight: bold;
}
.highlight {
    background-color: bisque;
    color: black;
    border-radius: 2px;
    padding: 0 3px;
    margin-right: 10px;
    font-size: 17px;
}

.section_title {
  padding-bottom: 2px;
  margin: 35px 10px 20px 10px;
  font-size: larger;
  font-weight: bold;
  color: rgb(0, 248, 174);
  border-bottom: 2px solid rgb(180, 255, 233);
}


.write-container {
  padding: 1px 0 0 0;
  background-color: rgb(54, 54, 58);
  border-radius: 5px;
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
    height: 45px;
    border-radius: 500%;
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
    border-radius: 15px 15px 15px 0;
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
}

#comment:hover {
  background-color: rgb(224, 224, 224);
}

#body {
  background-color: #1d252e;
    border: none;
    border-radius: 2px;
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
    border-radius: 2px;
    font-size: 14px;
    font-weight: 500;
    height: 28px;
    outline: none;
    padding: 8px 8px 8px 20px; /* add left padding */
    width: 100%;
    font: inherit;
    color: rgb(0, 0, 0);
    box-sizing: border-box;
    margin: 0 10px 0 10px;
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
  
    .postbutton {
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 15px;
    width: fit-content;
    margin: 10px 10px 10px 10px;
    background-color: rgba(0, 255, 76, 0.726);
    border-radius: 4px;
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.322);
    padding: 5px;
    transition: 0.2s all;
}

    .disabled {
    height: 30px;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 15px;
    width: 80px;
    margin: 10px 10px 10px 0;
    background-color: #94949425;
    border-radius: 4px;
    }

    .postbutton:hover {
      background-color: #94949425;
    }

    .buttonbox {
      display: flex;
      justify-content: flex-end;
      flex-direction: row;
    }

.title-for-story {
    margin: 0px 0px 0px 0px;
}
 
</style>