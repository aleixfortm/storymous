<template>
    <feed-container>
        <post-container
        v-if="post"
            :_id="post._id"
            :title="post.title"
            :content="post.preview"
            :username="post.username"
            :postComment="post.post_comment"
            :date="post.date"
            :imgName="post.random_img">
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
        <comment-container
          v-for="comment in comments"
          :key="comment._id"
          :_id="comment._id"
          :content="comment.content"
          :username="comment.username"
          :date="comment.date"
          :imgName="comment.random_img">
        </comment-container>
    </feed-container>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

import CommentContainer from "@/components/layout/CommentContainer.vue";
import FeedContainer from '@/components/layout/FeedContainer.vue';
import PostContainer from '@/components/layout/PostContainer.vue';

export default {
  components: {
    FeedContainer,
    PostContainer,
    CommentContainer
  },
  data() {
    return {
      post: null,
      comments: [],
      formcomment: "",
    }
  },
  mounted() {
    axios
      .get('https://api.npoint.io/786a14060decfb7e66d9')
      .then(response => {
        this.comments = response.data.comments;
        const posts1 = response.data.latest;
        const posts2 = response.data.following;

        const id = this.$route.params.id;
        console.log(id)

        const post1 = posts1.find(post => post._id.$oid === id);
        if (post1) {
          this.post = post1;
        } else {
          console.log('Post not found in latest');
        }

        const post2 = posts2.find(post => post._id.$oid === id);
        if (post2) {
          this.post = post2;
        } else {
          console.log('Post not found in following');
        }
        
      })
  },
  computed: {
    ...mapGetters("emitdata", ["getEmittedData"])
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