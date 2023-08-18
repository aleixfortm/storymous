<template>
    <feed-container>
        <div>This is the home sidebar</div>
    </feed-container>
</template>

<script>
import FeedContainer from '../frames/FeedContainer.vue';

export default {
    name: "HomeSidebar",
    components: {
        FeedContainer
    }
}
</script>

<style scoped>
div {
    color: white;
}
</style>