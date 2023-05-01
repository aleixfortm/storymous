<template>
    <section>
        <ul>
            <li>Global</li>
            <li>Following</li>
        </ul>
    </section>
    <feed-container></feed-container>
    <feed-container class="selector"></feed-container>
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

section {
    margin: auto;
    width: 50%;
    height: 40px;
    margin-top: 20px;
}

ul {
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

li {
    list-style: none;
    margin: auto 10px;
}


</style>