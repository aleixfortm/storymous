<template>
    <feed-container>
        <span v-if="!loading">
          <div v-if="posts.following.length >= 1">
            <div v-for="post in posts.following" :key="post._id">
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
                    :comments="post.user_comments"
                    :views="post.views"
                    :tags="post.tags"
                    :leaves="post.leaves"
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
                    :views="post.views"
                    :leaves="post.leaves"
                    :tags="post.tags">
                </continuestoryfeed-container>
              </template>
            </div>
          </div>
          <div v-else>
            <astronaut-message
            :onomatopoeia="'crick crick'"
            :text="`Looks like you aren't following anyone yet...`"
            ></astronaut-message>
          </div>
        </span>
        <span v-else class="loader-container">
          <div class="spinner-border text-light mb-3" style="width: 5rem; height: 5rem;" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <span class="loader-text">Looking for your friends...</span>
        </span>
    </feed-container>
</template>

<script>
import PostContainer from "@/components/feedposts/PostContainer.vue";
import FeedContainer from "@/components/frames/FeedContainer.vue";
import AstronautMessage from "@/components/messages/AstronautMessage.vue";
import ContinuestoryfeedContainer from "@/components/feedposts/ContinuestoryfeedContainer.vue";

export default {
    props: ["posts", "loading"],
    components: {
        PostContainer,
        FeedContainer,
        AstronautMessage,
        ContinuestoryfeedContainer
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
</style>