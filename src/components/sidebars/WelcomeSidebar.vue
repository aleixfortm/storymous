<template>
    <feed-container>
        <template v-if="!loading">
            <description-box></description-box>
            <topauthors-box></topauthors-box>
            <topstories-box></topstories-box>
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

export default {
    name: "WelcomeSidebar",
    components: {
        FeedContainer,
        DescriptionBox,
        TopauthorsBox,
        TopstoriesBox,
        EmptyBox
    },
    data() {
        return {
            loading: true
        }
    }
    

}
</script>

<style scoped>
div {
    color: white;
}
</style>