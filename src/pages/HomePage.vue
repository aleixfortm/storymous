<template>

        <div class="selector">
            <ul>
                <li>New</li>
                <li>Following</li>
            </ul>
        </div>

    <feed-container></feed-container>
    <feed-container></feed-container>
    <feed-container class="posts"></feed-container>
    <feed-container></feed-container>
</template>


<script>
import FeedContainer from "../components/layout/FeedContainer.vue"

export default {
    components: {
        FeedContainer
    }
}


</script>


<style scoped>

.selector {
    height: 100px;
}

ul {
    padding: 10px 100px;
}

li {
    list-style: none;
    width: 50%;
    justify-content: center;
    align-items: center;
    text-align: center;
}


</style>