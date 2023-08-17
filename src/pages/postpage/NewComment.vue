<template>
    <div class="add-comment-box">
        <form @submit.prevent="submitComment">
          <div class="pic__form">
            <div class="newstory_comment">
                <div class="image_box">
                    <img class="postimage" :src="imgSource" alt="profilepic">
                </div>
                <textarea id="comment" v-model="formcomment" placeholder="Add a comment..." rows="1" :style="{ height: textareaHeight }" required></textarea>
            </div>
          </div>
          <div class="buttonbox" v-if="writtenSomething">
            <newcomment-button :text="'Comment'" :buttonLoading="buttonLoading" :margin="true">
              <span class="material-symbols-outlined">chat_bubble</span>
            </newcomment-button>
          </div>
        </form>
    </div>
</template>

<script>
import axios from "axios";
import { API_BASE_URL } from '../../config';
import { mapGetters } from 'vuex'
import NewcommentButton from '@/components/UIcomponents/buttons/NewcommentButton.vue';

export default {
    components: {
        NewcommentButton
    },
    props: ["story_id"],
    data() {
        return {
            textareaHeight: null,
            formcomment: "",
            buttonLoading: false
        }
    },
    methods: {
        adjustTextareaHeight() {
          const textarea = this.$el.querySelector('#comment');
          textarea.style.height = 'auto';
          textarea.style.height = textarea.scrollHeight + 'px';
          this.textareaHeight = textarea.style.height;
        },
        submitComment() {
          const data_packet = {
            username: this.currentUser,
            comment: this.formcomment,
            story_id: this.story_id,
          }
          this.buttonLoading = true;
          axios
            .post(`${API_BASE_URL}/new_comment`, data_packet)
            .then(response => {
              this.buttonLoading = false;
              const dataPayload = response.data;
              this.replies.unshift(dataPayload.comment_data);
              this.formcomment = '';
            })
            .catch(error => {
              console.log(error);
            });
        },
    },
    watch: {
        formcomment() {
          this.formcomment = this.formcomment.substring(0, 300);
          this.adjustTextareaHeight();
        },
    },
    computed: {
      ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched"]),
      imgSource() {
        return require("@/assets/img/" + this.userFetchedPicture)
      },
      writtenSomething() {
        return this.formcomment.length > 0
      }
    }
}
</script>

<style scoped>
newcomment-button {
  display: flex;
  align-items: center;
}

.material-symbols-outlined {
  font-size: 20px;
}

.buttonbox {
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.add-comment-box {
  padding: 5px;
  background-color: rgba(126, 126, 126, 0.192);
  border-radius: 5px;
}

.newstory_comment {
  display: flex;
  align-items: center;
}

.image_box {
  height: fit-content;
  width: fit-content;
  margin: 0 8px 0 0;
}

.postimage {
  width: 40px;
  height: auto;
  border-radius: 500%;
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
  transition: 0.3s all;
}

#comment:hover {
  background-color: rgb(196, 196, 196);
}

</style>

