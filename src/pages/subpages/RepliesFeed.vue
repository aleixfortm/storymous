<template>
    <feed-container v-if="!loading">
        <div v-for="reply in replies" :key="reply._id">
            <template v-if="reply.type === 'comment'">
            <comment-container
                :_id="reply._id"
                :content="reply.comment"
                :username="reply.username"
                :date="reply.date"
                :picture="reply.picture"
            ></comment-container>
            </template>
            <template v-else>
            <continuestory-container
                :_id="reply._id"
                :storyId="reply.story_id"
                :parentChapterId="reply.parent_chapter_id"
                :content="reply.content"
                :chapterName="reply.chapter_name"
                :chapterNum="reply.chapter_num"
                :username="reply.username"
                :postComment="reply.comment"
                :date="reply.date"
                :picture="reply.picture"
                :tags="reply.tags"
            ></continuestory-container>
            </template>
        </div>
        <astronaut-message v-if="replies.length == 0" 
            :onomatopoeia="'crick crick'" 
            :text="'No comments or chapters have been written for this story yet. You can be the first, hurry up!'">
        </astronaut-message>
    </feed-container>
    <feed-container v-else>
      <div class="loader-container">
        <div class="spinner-border text-light mb-3" style="width: 5rem; height: 5rem;" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
          <span class="loader-text">Harvesting story from story tree</span>
      </div>
    </feed-container>
</template>

<script>
import CommentContainer from '@/components/layout/CommentContainer.vue';
import ContinuestoryContainer from '@/components/layout/ContinuestoryContainer.vue';
import AstronautMessage from '@/components/layout/messages/AstronautMessage.vue';
import FeedContainer from '@/components/layout/FeedContainer.vue';

export default {
    props: ["replies", "loading"],
    components: {
        CommentContainer,
        ContinuestoryContainer,
        AstronautMessage,
        FeedContainer
    }
}
</script>