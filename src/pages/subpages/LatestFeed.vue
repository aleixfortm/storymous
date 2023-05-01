<template>
    <post-container
    v-for="post in posts"
    :key="post.id"
    :title="post.title"
    :content="post.content"
    :username="post.username"
    :postComment="post.postComment"
    :date="post.date">
    </post-container>
</template>


<script>
import PostContainer from "../../components/layout/PostContainer.vue";

export default {
    inject: ["posts"],
    components: {
        PostContainer
    }
}

</script>