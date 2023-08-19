<template>
  <feed-container>
    <template v-if="loading">
        <load-container v-for="i in 6" :key="i"></load-container>
    </template>
    <div v-else v-for="post in posts" :key="post._id">
        <post-container
            :_id="post._id"
            :title="post.title"
            :content="post.content"
            :username="post.username"
            :postComment="post.comment"
            :chapterNum="post.chapter_num"
            :date="post.created_at"
            :picture="post.picture"
            :views="post.views"
            :tags="post.tags"
            :leaves="post.leaves"
            :story_name="post.story_name"
            :comments="post.comments"
            :feedMode="true">
        </post-container>
    </div>
  </feed-container>
</template>


<script>
import PostContainer from "@/components/feedposts/PostContainer.vue";
import FeedContainer from "@/components/frames/FeedContainer.vue";
//import LoaderComponent from "@/components/UIcomponents/LoaderComponent.vue";
import LoadContainer from "@/components/feedposts/LoadContainer.vue";

export default {
    props: ["posts", "loading"],
    components: {
        PostContainer,
        FeedContainer,
        LoadContainer
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