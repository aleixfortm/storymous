<template>
  <feed-container>
    <div v-if="loading" class="loader-container">
      <div class="spinner-border text-light mb-3" style="width: 5rem; height: 5rem;" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <span class="loader-text">Loading stories...</span>
    </div>
    <div v-else v-for="post in posts.latest" :key="post._id">
      <template v-if="post.type === 'prologue'">
        <post-container
            :_id="post._id"
            :title="post.title"
            :content="post.content"
            :username="post.username"
            :postComment="post.comment"
            :date="post.date"
            :picture="post.picture"
            :color="post.color"
            :views="post.views"
            :comments="post.user_comments"
            :tags="post.tags"
            :feedMode="true">
        </post-container>
      </template>
      <template v-else>
        <continuestoryfeed-container
        v-if="post.type === 'chapter'"
            :_id="post._id"
            :storyId="post.story_id"
            :parentChapterId="post.parent_chapter_id"
            :content="post.content"
            :chapterName="post.chapter_name"
            :chapterNum="post.chapter_num"
            :username="post.username"
            :color="post.color"
            :storyTitle="post.story_title"
            :postComment="post.comment"
            :date="post.date"
            :picture="post.picture"
            :tags="post.tags">
        </continuestoryfeed-container>
      </template>
    </div>
  </feed-container>
</template>


<script>
import PostContainer from "@/components/layout/feedposts/PostContainer.vue";
import ContinuestoryfeedContainer from "@/components/layout/feedposts/ContinuestoryfeedContainer.vue";
import FeedContainer from "@/components/layout/FeedContainer.vue";

export default {
    props: ["posts", "loading"],
    components: {
        PostContainer,
        ContinuestoryfeedContainer,
        FeedContainer
    },
    methods: {
        formatContent(text) {
            return text.replace(/<br>/g, '\n');
        }
    },
    mounted() {

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

</style>