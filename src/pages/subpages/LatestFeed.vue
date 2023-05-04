<template>
    <post-container
    v-for="post in posts"
    :key="post._id"
    :title="post.title"
    :content="post.preview"
    :username="post.username"
    :postComment="post.post_comment"
    :date="post.date"
    :extendedLength="post.extended_length">
    </post-container>
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