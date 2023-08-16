<template>
    <feed-container v-if="!loading">
        <div v-for="chapter in chapters" :key="chapter._id">
            <continuestory-container
                @selected-chapter="emitSelectedChapter"
                :chapter="chapter"
            ></continuestory-container>
        </div>
        <astronaut-message v-if="chapters.length === 0" 
            :onomatopoeia="'crick crick'" 
            :text="'No comments or chapters have been written for this story yet. You can be the first, hurry up!'">
        </astronaut-message>
    </feed-container>
    <feed-container v-else>
        <loader-component :text="'Harvesting chapters'"></loader-component>
    </feed-container>
</template>

<script>
import ContinuestoryContainer from '@/components/postreplies/ContinuestoryContainer.vue';
import AstronautMessage from '@/components/messages/AstronautMessage.vue';
import FeedContainer from '@/components/frames/FeedContainer.vue';
import LoaderComponent from '@/components/UIcomponents/LoaderComponent.vue';

export default {
    props: ["loading", "chapters"],
    components: {
        ContinuestoryContainer,
        AstronautMessage,
        FeedContainer,
        LoaderComponent
    },
    methods: {
        emitSelectedChapter(data) {
            this.$emit("selected-chapter", data);
        }
    }
}
</script>