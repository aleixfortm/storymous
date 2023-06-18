<template>
    <feed-container>
        <post-container
            :key="post._id"
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
import PostContainer from "@/components/layout/PostContainer.vue";
import FeedContainer from "../components/layout/FeedContainer.vue"

export default {
    data() {
        return {
            PostContainer,
            FeedContainer
        }
    }
}

</script>

