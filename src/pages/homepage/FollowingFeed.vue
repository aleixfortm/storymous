<template>
    <feed-container>
        <span v-if="!loading">
          <div v-if="posts.following.length >= 1">
            <div v-for="post in posts.following" :key="post._id">
              <post-container
                  :_id="post._id"
                  :title="post.title"
                  :content="post.content"
                  :username="post.username"
                  :postComment="post.comment"
                  :date="post.created_at"
                  :picture="post.picture"
                  :views="post.views"
                  :tags="post.tags"
                  :leaves="post.leaves"
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
        <loader-component v-else :text="'Looking for your friends...'"></loader-component>
    </feed-container>
</template>

<script>
import PostContainer from "@/components/feedposts/PostContainer.vue";
import FeedContainer from "@/components/frames/FeedContainer.vue";
import AstronautMessage from "@/components/messages/AstronautMessage.vue";
import LoaderComponent from "@/components/UIcomponents/LoaderComponent.vue";

export default {
    props: ["posts", "loading"],
    components: {
        PostContainer,
        FeedContainer,
        AstronautMessage,
        LoaderComponent
    },
    methods: {
        formatContent(text) {
            return text.replace(/<br>/g, '\n');
        }
    }
}
</script>