<template>
    <div class="entirebox">
        <div class="box">
            <div class="explanation">
                <div class="title-num-container">
                    <div class="title">Contributors</div>
                    <div class="number">{{ contributors.length }}</div>
                </div>
                <user-data v-for="author in contributors" :user="author" :key="author"></user-data>
            </div>
        </div>
    </div>
</template>

<script>
import UserData from "./UserData.vue"

export default {
    name: "ContributorsBox",
    props: ["contributors"],
    components: {
        UserData
    },
    data() {
        return {
            topUsers: [
                {
                    username: "stoupeaks",
                    picture: "astronaut_looking_earth.jpeg",
                    leaves: 23
                },
                {
                    username: "benetti",
                    picture: "astronaut_saloon.jpeg",
                    leaves: 19
                },
                {
                    username: "Lil_Metro",
                    picture: "default_orange.png",
                    leaves: 13
                },
                {
                    username: "stoupeaks",
                    picture: "astronaut_looking_earth.jpeg",
                    leaves: 23
                },
                {
                    username: "benetti",
                    picture: "astronaut_saloon.jpeg",
                    leaves: 19
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

.title-num-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.entirebox {
    margin-top: 10px;
}

.marginated {
    margin-top: 5px;
    line-height: 1.05 !important;
}

.number {
    font-weight: bold;
    font-size: 14px;
    padding: 0px 4px;
    background-color: rgba(161, 161, 161, 0.212);
    border-radius: 10px;
}

.box {
    height: fit-content;
    width: 100%;
    text-align: left;
    padding: 8px;
    border-radius: 4px;
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
