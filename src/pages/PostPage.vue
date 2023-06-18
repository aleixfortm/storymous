<template>
    POLLANCRERA <br><br>LOLOLOLOLOLO
    <post-container
        :key="post._id"
        :_id="post._id"
        :title="post.title"
        :username="post.username"
        :postComment="post.post_comment"
        :date="post.date"
        :imgName="post.random_img"
        @post-selected="handleSelectedPost()">
    </post-container>

</template>

<script>
import PostContainer from "../components/layout/PostContainer.vue";

export default {
    data() {
        return {
            PostContainer
        }
    },
    methods: {
        handleSelectedPost() {
            console.log("pollancre")
        }
    },
}

</script>

