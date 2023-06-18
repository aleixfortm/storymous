<template>
    <feed-container>
        POLLANCRERA <br><br><br><br>LOLOLOLOLOLO
        <post-container

            @post-selected="handleSelectedPost()">
        </post-container>
    </feed-container>
</template>

<script>
import PostContainer from "../components/layout/PostContainer.vue";
import FeedContainer from "../components/layout/FeedContainer.vue"

export default {
    data() {
        return {
            PostContainer,
            FeedContainer
        }
    },
    methods: {
        handleSelectedPost(post) {
            console.log(post)
        }
    },
}

</script>

