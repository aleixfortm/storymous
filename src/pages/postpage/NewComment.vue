<template>
    <div class="add-comment-box">
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
</template>

<script>
import CommentButton from '@/components/UIcomponents/buttons/CommentButton.vue';

export default {
    components: {
        CommentButton
    },
    data() {
        return {
            textareaHeight: null,
            formcomment: "",
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

</style>

