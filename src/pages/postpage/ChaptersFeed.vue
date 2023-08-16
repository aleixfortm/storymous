<template>
    <feed-container v-if="!loading">
        <div v-for="reply in replies" :key="reply._id">
            <template v-if="reply.type === 'chapter' && !chapterList.some(obj => obj._id.$oid === reply._id.$oid)">
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
        <astronaut-message v-if="replies.length > 0" 
            :onomatopoeia="'crick crick'" 
            :text="'No comments or chapters have been written for this story yet. You can be the first, hurry up!'">
        </astronaut-message>
    </feed-container>
    <feed-container v-else>
        <loader-component :text="'Harvesting chapters...'"></loader-component>
    </feed-container>
</template>

<script>
import ContinuestoryContainer from '@/components/postreplies/ContinuestoryContainer.vue';
import AstronautMessage from '@/components/messages/AstronautMessage.vue';
import FeedContainer from '@/components/frames/FeedContainer.vue';
import LoaderComponent from '@/components/UIcomponents/LoaderComponent.vue';

export default {
    props: ["replies", "loading", "chapterList"],
    components: {
        ContinuestoryContainer,
        AstronautMessage,
        FeedContainer,
        LoaderComponent
    },
    computed: {
        hasValidReplies() {
            return this.replies.some(reply => {
                return reply.type === 'chapter' && !this.chapterList.some(obj => obj._id === reply._id);
            });
        }
    }
}
</script>