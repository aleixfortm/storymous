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
            :extendedLength="post.extended_length"
            :imgName="post.random_img">
        </post-container>
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
//import { mapGetters } from "vuex";

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
      emittedData: null
    }
  },
  mounted() {
    axios
      .get('https://api.npoint.io/786a14060decfb7e66d9')
      .then(response => {
        this.comments = response.data.comments;
        this.post = response.data.latest[0];
      })
    },

}
</script>