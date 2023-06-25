<template>
    <feed-container>
        <post-container
          v-if="post"
            :_id="post._id"
            :title="post.title"
            :content="post.content"
            :username="post.username"
            :postComment="post.post_comment"
            :date="post.date"
            :picture="post.picture"
            :color="post.color">
        </post-container>
        <div class="pollancre">
            <form @submit.prevent="submitForm">
                <div class="newstory_comment">
                    <div class="image_box">
                        <img class="postimage" src="../assets/img/default_blue.png" alt="profilepic">
                    </div>
                    <textarea id="comment" v-model="formcomment" placeholder="Add a comment..." rows="1" :style="{ height: textareaHeight }" required></textarea>
                    <div class="buttonbox">
                      <button class="postbutton" type="submit">Comment</button>
                    </div>
                </div>
            </form>
        </div>
        <div v-if="replies">
          <comment-container 
            v-for="reply in replies"
              :key="reply._id"
              :_id="reply._id"
              :content="reply.content"
              :username="reply.username"
              :date="reply.date"
              :picture="reply.picture">
          </comment-container>
        </div>
        <!--
        <continuestory-container
        v-if="replyPost"
            :_id="replyPost._id"
            :content="replyPost.content"
            :username="replyPost.username"
            :postComment="replyPost.postComment"
            :date="replyPost.date"
            :picture="replyPost.imgName">
        </continuestory-container>
        -->
    </feed-container>
</template>

<script>
import axios from "axios";

import CommentContainer from "@/components/layout/CommentContainer.vue";
//import ContinuestoryContainer from "@/components/layout/ContinuestoryContainer.vue";
import FeedContainer from '@/components/layout/FeedContainer.vue';
import PostContainer from '@/components/layout/PostContainer.vue';

export default {
  components: {
    FeedContainer,
    PostContainer,
    CommentContainer,
    //ContinuestoryContainer
  },
  data() {
    return {
      post: null,
      replies: null,
      formcomment: "",
      continuedStory: null,
      textareaHeight: null,
    }
  },
  mounted() {
    const postId = this.$route.params.id;
    axios
      .get(`http://192.168.1.44:5000/post/${postId}`)
      .then(response => {

        this.post = response.data.post;
        console.log(this.post)
        this.replies = response.data.replies;

      })
  },
  computed: {

  },
  methods: {
    adjustTextareaHeight() {
          const textarea = this.$el.querySelector('#comment');
          textarea.style.height = 'auto';
          textarea.style.height = textarea.scrollHeight + 'px';
          this.textareaHeight = textarea.style.height;
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


    .postbutton {
    height: 35px;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(0, 255, 98);
    cursor: pointer;
    font-size: 15px;
    width: 80px;
    margin: 0px 5px 7px 0;
    background-color: #ffffff1e;
    border-radius: 4px;
    align-self: flex-end;
  }

  .postbutton:hover {
    background-color: #94949425;
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
}

#comment:hover {
  background-color: rgb(224, 224, 224);
}

.pollancre {
  padding: 1px 0 0 0;
  background-color: rgb(119 119 119 / 19%);
  border-radius: 10px;
  margin: 5px 0 12px 0;
}

.newstory_comment {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: fit-content;
    padding: 5px 0 5px 0;
    display: flex;
    justify-content: left;
    border-radius: 10px;
    align-items: center;
}

.image_box {
    height: max-content;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-self: start;
}

.buttonbox {
  align-self: stretch;
  display: flex;
  }

  .postimage {
    height: 50px;
    border-radius: 100%;
    margin: 0px 8px 0 10px;
    cursor: pointer;
    transition: all 0.1s;
}

.postimage:hover {  
  filter: brightness(85%);
}
</style>