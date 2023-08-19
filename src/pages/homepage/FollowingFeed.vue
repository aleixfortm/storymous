<template>
    <feed-container>
        <span v-if="!loading">
          <div v-if="handleFollowingPosts.length >= 1">
            <div v-for="post in handleFollowingPosts" :key="post._id">
              <post-container
                  :_id="post._id"
                  :title="post.title"
                  :content="post.content"
                  :username="post.username"
                  :postComment="post.comment"
                  :date="post.created_at"
                  :chapterNum="post.chapter_num"
                  :picture="post.picture"
                  :views="post.views"
                  :tags="post.tags"
                  :leaves="post.leaves"
                  :story_name="post.story_name"
                  :comments="post.comments"
                  :feedMode="true">
              </post-container>
            </div>
          </div>
          <div v-else>
            <astronaut-message
            :onomatopoeia="'crick crick'"
            :text="`Looks like you aren't following anyone yet...`"
            ></astronaut-message>
          </div>
        </span>
        <template v-else>
          <load-container v-for="i in 6" :key="i"></load-container>
        </template>
    </feed-container>
</template>

<script>
import PostContainer from "@/components/feedposts/PostContainer.vue";
import FeedContainer from "@/components/frames/FeedContainer.vue";
import AstronautMessage from "@/components/messages/AstronautMessage.vue";
import LoadContainer from "@/components/feedposts/LoadContainer.vue";
import { mapGetters } from 'vuex';

export default {
    props: ["posts", "loading"],
    components: {
        PostContainer,
        FeedContainer,
        AstronautMessage,
        LoadContainer
    },
    methods: {
        formatContent(text) {
            return text.replace(/<br>/g, '\n');
        }
    },
    computed: {
      ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched", "userFetchedBio", "nFetchedPosts", "nFetchedFollowers", "nFetchedFollowing", "nFetchedLeaves"]),
      handleFollowingPosts() {
        const filteredPosts = this.posts.filter(post => this.nFetchedFollowing.includes(post.username));
        return filteredPosts
      }
    },
}
</script>