<template>
    <feed-container>
        <post-container
        v-if="post"
            :key="post._id"
            :_id="post._id"
            :title="post.title"
            :content="post.preview"
            :username="post.username"
            :postComment="post.post_comment"
            :date="post.date"
            :extendedLength="post.extended_length"
            :imgName="post.random_img">
        </post-container>
    </feed-container>
</template>

<script>
import axios from "axios";
import FeedContainer from '@/components/layout/FeedContainer.vue';
import PostContainer from '@/components/layout/PostContainer.vue';

export default {
  components: {
    FeedContainer,
    PostContainer
  },
  data() {
    return {
      post: null
    }
  },
  mounted() {
    axios
      .get('https://api.npoint.io/786a14060decfb7e66d9')
      .then(response => {
        //console.log(response.data.latest[4])
        this.post = response.data.latest[0]; // Assuming you want to display the first post
      })
    }
}
</script>