<template>
    <feed-container>
        <description-box>

        </description-box>
    </feed-container>
</template>

<script>
import FeedContainer from '../frames/FeedContainer.vue';
import DescriptionBox from "./welcome/DescriptionBox.vue"

export default {
    name: "WelcomeSidebar",
    components: {
        FeedContainer,
        DescriptionBox
    },
    

}
</script>

<style scoped>
div {
    color: white;
}
</style>