<template>
  <feed-container>
    <loader-component v-if="loading" :text="'Loading stories...'"></loader-component>
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
            :leaves="post.leaves"
            :views="post.views"
            :tags="post.tags">
        </continuestoryfeed-container>
      </template>
    </div>
  </feed-container>
</template>


<script>
import PostContainer from "@/components/feedposts/PostContainer.vue";
import ContinuestoryfeedContainer from "@/components/feedposts/ContinuestoryfeedContainer.vue";
import FeedContainer from "@/components/frames/FeedContainer.vue";
import LoaderComponent from "@/components/UIcomponents/LoaderComponent.vue";

export default {
    props: ["posts", "loading"],
    components: {
        PostContainer,
        ContinuestoryfeedContainer,
        FeedContainer,
        LoaderComponent
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