<template>
    <feed-container>
        <div v-if="posts.following.length >= 1">
            <post-container
                v-for="post in posts.following"
                :key="post._id"
                :_id="post._id"
                :title="post.title"
                :content="post.content"
                :username="post.username"
                :postComment="post.comment"
                :date="post.date"
                :picture="post.picture"
                :color="post.color"
                :feedMode="true">
            </post-container>
        </div>
        <div v-else>
            <div class="imagecontainer">
                <div class="onomatopoeia">crick crick</div>
                <img class="astronaut-image" src="../../assets/img/astronaut_reading_space_nostars.png" alt="astronaut floating">
                <div class="loader-text">Looks like you aren't following anyone yet...</div>
            </div>
        </div>
    </feed-container>
</template>

<script>
import PostContainer from "../../components/layout/PostContainer.vue";
import FeedContainer from "@/components/layout/FeedContainer.vue";

export default {
    props: ["posts"],
    components: {
        PostContainer,
        FeedContainer
    },
    methods: {
        formatContent(text) {
            return text.replace(/<br>/g, '\n');
        }
    }
}
</script>

<style scoped>
.onomatopoeia {
    color: whitesmoke;
    font-weight: bold;
    font-size: 14px;
    margin-bottom: -10px;
}

@keyframes floatAnimation {
  0% {
    transform: translateY(-5px);
  }
  50% {
    transform: translateY(5px);
  }
  100% {
    transform: translateY(-5px);
  }
}

.astronaut-image {
    width: 175px;
    height: auto;
    animation: floatAnimation 4s ease-in-out infinite;
}

.imagecontainer {
    margin: 50px auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: fit-content;
}

.loader-text {
    background-color: whitesmoke;
    text-align: center;
    color: rgb(0, 0, 0);
    padding: 5px 10px;
    border-radius: 15px;
    font-weight: bold;
    margin: 0 10px;
}
</style>