<template>
    <div class="write-container">
        <form @submit.prevent="submitForm">
            <div class="newstory_comment">
                <div class="image_box">
                    <img class="postimage" v-if="userFetchedPicture" :src="imgSource" alt="profilepic">
                </div>
                <div class="extended-container">
                    <textarea id="comment" v-model="formcomment" placeholder="Author comment" rows="1" :style="{ height: textareaHeight }" required></textarea>
                    <span class="story__user-name3"><b>@{{ username }}</b> · Now</span>
                </div>
            </div>
            <div class="newstory_title marginated">

                <input id="title" class="title-for-story" v-model="formtitle" type="text" placeholder="Chapter name" required>
            </div>
            <div class="newstory_title">
                <textarea id="body" v-model="formbody" placeholder="Chapter content" required></textarea>
            </div>
            <div class="buttonbox">
                <button :class="{ 'postbutton': true, 'disabled': isPostButtonDisabled }" :disabled="isPostButtonDisabled" type="submit">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
  import { API_BASE_URL } from '../../config';

  import axios from 'axios';
import router from '@/router';

  export default {
    name: "NewPost",
    props: ["chapterNum", "username", "postId"],
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
          body: this.formbody,
          username: this.currentUser,
          postId: this.postId.$oid
        }

        console.log(data_packet)
        axios.post(`${API_BASE_URL}/new_chapter`, data_packet)
        .then(response => {
            this.loading = false;
            const data = response.data;
            if (data.status === "Success") {
                this.isPostButtonDisabled = true;
                router.push("/chapter/" + data.chapter_id)
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
          return require('../../assets/img/' + this.userFetchedPicture);
        },
        postButtonText() {
            return this.isPostButtonDisabled ? "Submitted" : "Submit?"
        }
    }
  };

</script>

<style scoped>
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
    margin: 0px 0px 0px 12px;
    min-width: 100px;
    background-color: rgb(0, 132, 255);
    border-radius: 4px;
    padding: 0 3px;
    margin: 0 0px 0 0px;
    font-size: 17px;
    box-shadow: 0px 0px 5px 0px rgb(0, 132, 255);
    align-items: center;
    text-align: center;
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
  background-color: rgb(43, 43, 46);
  border-radius: 10px;
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