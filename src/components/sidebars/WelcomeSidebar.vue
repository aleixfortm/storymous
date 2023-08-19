<template>
    <feed-container>
        <template v-if="topAuthors.length > 0">
            <description-box></description-box>
            <topauthors-box :authors="topAuthors"></topauthors-box>
            <topstories-box :stories="topStories"></topstories-box>
        </template>       
        <template v-else>
            <empty-box v-for="i in 3" :key="i"></empty-box>
        </template>
    </feed-container>
</template>

<script>
import FeedContainer from '../frames/FeedContainer.vue';
import DescriptionBox from "./welcome/DescriptionBox.vue";
import TopauthorsBox from './welcome/TopauthorsBox.vue';
import TopstoriesBox from './welcome/TopstoriesBox.vue';
import EmptyBox from "./boxes/EmptyBox.vue"
import { mapGetters } from 'vuex';

export default {
    name: "WelcomeSidebar",
    components: {
        FeedContainer,
        DescriptionBox,
        TopauthorsBox,
        TopstoriesBox,
        EmptyBox
    },
    computed: {
        ...mapGetters('topData', ['topAuthors', 'topStories']),
    },
    

}
</script>

<style scoped>
div {
    color: white;
}
</style>