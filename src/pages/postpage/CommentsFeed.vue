<template>
    <feed-container v-if="!loading">
        <div v-for="comment in comments" :key="comment._id">
            <comment-container
                :_id="comment._id"
                :content="comment.comment"
                :username="comment.username"
                :date="comment.date"
                :picture="comment.picture"
            ></comment-container>
        </div>
        <astronaut-message v-if="comments.length === 0" 
            :onomatopoeia="'crick crick'" 
            :text="'No comments or chapters have been written for this story yet. You can be the first, hurry up!'">
        </astronaut-message>
    </feed-container>
    <feed-container v-else>
        <loader-component :text="'Fetching all comments'"></loader-component>
    </feed-container>
</template>

<script>
import CommentContainer from '@/components/postreplies/CommentContainer.vue';
import AstronautMessage from '@/components/messages/AstronautMessage.vue';
import FeedContainer from '@/components/frames/FeedContainer.vue';
import LoaderComponent from '@/components/UIcomponents/LoaderComponent.vue';

export default {
    props: ["comments", "loading"],
    components: {
        CommentContainer,
        AstronautMessage,
        FeedContainer,
        LoaderComponent
    }
}
</script>