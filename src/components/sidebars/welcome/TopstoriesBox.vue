<template>
    <div class="entirebox">
        <div class="box">
            <div class="explanation">
                <div class="title">Most read stories</div>
                <story-data v-for="story in topStories" :story="story" :key="story"></story-data>
            </div>
        </div>
    </div>
</template>

<script>
import StoryData from './StoryData.vue';

export default {
    name: "DescriptionBox",
    components: {
        StoryData
    },
    data() {
        return {
            topStories: [
                {
                    username: "benetti",
                    picture: "astronaut_saloon.jpeg",
                    story_title: "The quest of CSGO",
                    views: 821
                },
                {
                    username: "Lil_metro",
                    picture: "default_orange.png",
                    story_title: "Albertitou Gilipollitou Series",
                    views: 720
                },
                {
                    username: "Alverd",
                    picture: "astronaut_reading.jpeg",
                    story_title: "Road to Grandmaster",
                    views: 543
                },
            ]
        }
    },
    computed: {
        imgSrc() {
            return require("@/assets/img/storymous-forest-min.png")
        }
    }
}
</script>

<style scoped>

.extra {
    padding: 2px 6px;
    font-size: 12px;
}

.entirebox {
    margin-top: 10px;
}

.marginated {
    margin-top: 5px;
    line-height: 1.05 !important;
}

.box {
    height: fit-content;
    width: 100%;
    text-align: left;
    padding: 8px;
    border-radius: 5px;
    border: 1px rgba(255, 255, 255, 0.247) solid;
    background-color: rgba(43, 43, 46, 0.671);
    transition: 0.2s all;
}

.title {
    font-weight: bold;
    font-size: 14px;
}

.data-section {
    margin-top: 5px;
    padding: 2px 6px;
    background-color: rgba(92, 92, 92, 0.438);
    border-radius: 5px;
}

.data {
    font-size: 14px;
    line-height: 1.05 !important;
    margin-top: 3px;
}

.tree-image {
    width: 100%;
    border-radius: 5px 5px 0 0;
    border: 1px rgba(255, 255, 255, 0.247) solid;
    border-bottom: none;
}
</style>
