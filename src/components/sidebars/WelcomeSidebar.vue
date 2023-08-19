<template>
    <feed-container>       
        <description-box></description-box>
        <topauthors-box></topauthors-box>
        <topstories-box></topstories-box>
        
    </feed-container>
</template>

<script>
import FeedContainer from '../frames/FeedContainer.vue';
import DescriptionBox from "./welcome/DescriptionBox.vue";
import TopauthorsBox from './welcome/TopauthorsBox.vue';
import TopstoriesBox from './welcome/TopstoriesBox.vue';

export default {
    name: "WelcomeSidebar",
    components: {
        FeedContainer,
        DescriptionBox,
        TopauthorsBox,
        TopstoriesBox
    },
    

}
</script>

<style scoped>
div {
    color: white;
}
</style>