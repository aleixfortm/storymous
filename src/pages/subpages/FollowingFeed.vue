<template>
    <feed-container>
        <post-container
            v-for="post in posts.following"
            :key="post._id"
            :_id="post._id"
            :title="post.title"
            :content="post.content"
            :username="post.username"
            :postComment="post.post_comment"
            :date="post.date"
            :picture="post.picture"
            :color="post.color">
        </post-container>
    </feed-container>
</template>

<script>
import PostContainer from "../../components/layout/PostContainer.vue";

export default {
    props: ["posts"],
    components: {
        PostContainer
    },
    methods: {
        formatContent(text) {
            return text.replace(/<br>/g, '\n');
        }
    }
}
</script>