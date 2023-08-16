<template>
  <feed-container>
    <loader-component v-if="loading" :text="'Loading stories'"></loader-component>
    <div v-else v-for="post in posts.latest" :key="post._id">
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
  </feed-container>
</template>


<script>
import PostContainer from "@/components/feedposts/PostContainer.vue";
import FeedContainer from "@/components/frames/FeedContainer.vue";
import LoaderComponent from "@/components/UIcomponents/LoaderComponent.vue";

export default {
    props: ["posts", "loading"],
    components: {
        PostContainer,
        FeedContainer,
        LoaderComponent
    },
    methods: {
        formatContent(text) {
            return text.replace(/<br>/g, '\n');
        }
    },
    mounted() {

    }
}

</script>