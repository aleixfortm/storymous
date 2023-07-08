<template>
    <feed-container>
        <span v-if="!loading">
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
        </span>
        <span v-else class="loader-container">
            <div class="lds-facebook">
                <div></div>
                <div></div>
                <div></div>
            </div>
            <span class="loader-text">Looking for your friends...</span>
        </span>
    </feed-container>
</template>

<script>
import PostContainer from "../../components/layout/PostContainer.vue";
import FeedContainer from "@/components/layout/FeedContainer.vue";

export default {
    props: ["posts", "loading"],
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
.loader-text {
    background-color: whitesmoke;
    color: rgb(0, 0, 0);
    padding: 5px 10px;
    border-radius: 15px;
    font-weight: bold;
}

.loader-container {
    margin: 40px 0 0 0;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.lds-facebook {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-facebook div {
  display: inline-block;
  position: absolute;
  left: 8px;
  width: 16px;
  background: #fff;
  animation: lds-facebook 1.2s cubic-bezier(0, 0.5, 0.5, 1) infinite;
}
.lds-facebook div:nth-child(1) {
  left: 8px;
  animation-delay: -0.24s;
}
.lds-facebook div:nth-child(2) {
  left: 32px;
  animation-delay: -0.12s;
}
.lds-facebook div:nth-child(3) {
  left: 56px;
  animation-delay: 0;
}
@keyframes lds-facebook {
  0% {
    top: 8px;
    height: 64px;
  }
  50%, 100% {
    top: 24px;
    height: 32px;
  }
}


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
    text-align: center;
    color: black;
    padding: 5px 10px;
    border-radius: 15px;
    font-weight: bold;
    margin: 0 10px;
}
</style>