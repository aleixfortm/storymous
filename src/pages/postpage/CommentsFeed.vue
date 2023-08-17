<template>
    <feed-container v-if="!loading">
        <new-comment v-if="isLoggedIn" @received-comment="handleNewComment" :story_id="story_id"></new-comment>
        <TransitionGroup name="list" tag="ul">
            <div v-for="comment in comments" :key="comment._id">
                <comment-container
                    :_id="comment._id"
                    :content="comment.comment"
                    :username="comment.username"
                    :date="comment.date"
                    :picture="comment.picture"
                ></comment-container>
            </div>
        </TransitionGroup>
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
import { mapGetters } from 'vuex';
import CommentContainer from '@/components/postreplies/CommentContainer.vue';
import AstronautMessage from '@/components/messages/AstronautMessage.vue';
import FeedContainer from '@/components/frames/FeedContainer.vue';
import LoaderComponent from '@/components/UIcomponents/LoaderComponent.vue';
import NewComment from "@/pages/postpage/NewComment.vue";

export default {
    props: ["comments", "loading", "story_id"],
    data() {
        return {
            mutableComments: this.comments
        }
    },
    components: {
        CommentContainer,
        AstronautMessage,
        FeedContainer,
        LoaderComponent,
        NewComment
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched"]),
    },
    methods: {
        handleNewComment(data) {
            this.mutableComments.unshift(data)
        }
    }
}
</script>

<style scoped>
ul {
  padding: 0;
  margin: 0;
}

.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}
</style>