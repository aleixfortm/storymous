<template>
    <div v-if="loading" class="loader-container">
        <div class="lds-facebook">
            <div></div>
            <div></div>
            <div></div>
        </div>
        <span class="loader-text">Harvesting stories...</span>
    </div>
    <div v-else>
        <post-container
        v-for="post in posts.latest"
            :key="post._id"
            :_id="post._id"
            :title="post.title"
            :content="post.content"
            :username="post.username"
            :postComment="post.post_comment"
            :date="post.date"
            :picture="post.picture"
            :color="post.color"
            :feedMode="true">
        </post-container>
    </div>
</template>


<script>
import PostContainer from "../../components/layout/PostContainer.vue";

export default {
    props: ["posts", "loading"],
    components: {
        PostContainer
    },
    methods: {
        formatContent(text) {
            return text.replace(/<br>/g, '\n');
        }
    }
}

</script>

<style>
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

</style>