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
      comments: []
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
  }

}
</script>