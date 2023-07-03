<template>
    <div class="background-story-reply2">
        <router-link to="" @click="navigateToPost" style="text-decoration: none;" >
            <div class="box1">
                <div class="sum-icon-container2">
                    <img src="../../assets/img/plus_icon4.png" alt="Plus icon" class="sum-icon2">
                </div>
                <div class="box2">
                    <div class="origin-container">
                        <div :class="['origin', chapterNum > 1 ? 'unmountable' : '']">Chapter {{ chapterNum }}</div>
                        <div v-if="tags.includes('End')" class="origin end">End</div>
                    </div>
                    <div class="story__user-container2">
                        <div class="story__user-img-container2">
                            <router-link to="" @click.stop="navigateToUser" style="color: inherit; text-decoration: none;">
                                <img :src="imgSource" alt="pic" class="story__user-img2">
                            </router-link>
                        </div> 
                        <div class="story__user-info-container2">
                            <div class="story__username2 cur-pnt"> 
                                <router-link to="" @click.stop="navigateToUser" style="color: inherit; text-decoration: none;">
                                    <span class="lower" style="color: whitesmoke;"><b>@</b></span><b class="story__user-name2">{{ username }}</b>
                                </router-link>
                                    <span class="story__username-date2 lower cur-def">· {{ date }} </span>
                            </div>
                            <div class="story__user-comment-container2"><div class="story__user-comment2 cur-def"> {{ postComment }} </div></div>
                        </div>
                    </div>
                </div>
            </div>
            <article class="story__article2">
                <div class="story__upper">
                    <h2 class="story__title "><span class="story_title highlight">{{ chapterNum }}</span>{{ chapterName }}</h2>
                </div>  
                <p class="story__content2">
                    {{ formatStory(content) }}
                </p>
            </article>
        </router-link>
    </div>
</template>

<script>
import { useRouter } from 'vue-router';
import { mapActions } from "vuex";

export default {
    setup() {
        const router = useRouter();
        return { router: router };
    },
    props: ["_id", "content", "username", "postComment", "date", "picture", "chapterNum", "storyId", "parentChapterId", "chapterName", "tags"],
    methods: {
        formatStory(story) {
            return story.replace(/<br>/g, '\n');
        },
        ...mapActions("emitdata", ["emitData"]),
        navigateToPost() {
            const dataToEmit =  {
                _id: this._id,
                content: this.content,
                username: this.username,
                postComment: this.postComment,
                date: this.date,
                picture: this.picture
            };
            this.emitData(dataToEmit);
            this.router.push('/chapter/' + this._id.$oid);
        },
        navigateToUser() {
            this.router.push('/user/' + this.username);
        }
    },
    computed: {
        imgSource() {
            return require('../../assets/img/' + this.picture);
        },
    },
    mounted() {

    }
};
</script>

<style scoped>


.highlight {
    background-color: rgba(255, 115, 0, 0.438);
    border-radius: 40px;
    padding: 0 5px;
    margin: 0 5px 0 -5px;
    font-size: 17px;
}

.story__upper {
    display: flex;
    margin: 5px 0 5px 0;

}   

.story__title {
    color: bisque;
    font-size: 17px;
    align-self: center;
    justify-self: center;
    margin: 0px 0px 0px 5px;

}

.box2 {
    display: flex;
    flex-direction: column;
}

.box1 {
    display: flex;
    flex-direction: row;
}

.origin {
    background-color: rgba(160, 255, 157, 0.753);
    font-weight: bold;
    color: rgb(3, 83, 0);
    font-size: 14px;
    padding: 1px 5px;
    border-radius: 3px;
    width: fit-content;
    box-shadow: 0px 0px 5px 0px rgba(13, 255, 0, 0.568);
    margin: 0 10px 0 0;
}

.unmountable {
    background-color: rgb(255, 125, 125);
    color: rgb(121, 24, 0);
    box-shadow: 0px 0px 5px 0px rgba(255, 130, 130, 0.568);
}

.end {
    background-color: rgb(192, 165, 255);
    color: rgb(141, 0, 184);
    box-shadow: 0px 0px 5px 0px rgba(164, 125, 255, 0.568);
}

.origin-container {
    display: flex;
    justify-content: flex-start;
    margin: 1px 5px 5px 2px;
}

.sum-icon-container2 {
    margin: 30px 3px 0 0;
}

.sum-icon2{
    max-width: 16px;
    margin: 0px;
}

.background-story-reply2 {
    background-color: rgba(110, 110, 110, 0.199);
    padding: 5px;
    margin: 8px 0 0 0;
    border-radius: 10px;
    transition: 0.1s all;
}

.background-story-reply2:hover {
    background-color: rgba(167, 167, 167, 0.199);
}

.background-story-reply2:active {
    background-color: rgba(167, 167, 167, 0.199);
}


.story__article2 {
    padding: 5px 10px;
    border-radius: 2px;
    cursor: pointer;
    transition: all 0s;
    background-color: rgb(46, 46, 53);
    color: rgb(223, 223, 223);
    font-weight: 400;
    text-align: left;
}


.story__user-container2 {
    padding: 0px 5px 2px 0px;
    display: flex;
    flex-direction: row;
}

.story__user-img-container2 {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.story__user-comment-container2 {
    max-width: fit-content;
    word-wrap: break-word;
}

.story__user-comment2 {
    margin-top: 0px;
    font-weight: bold;
    color: black;
    background-color: #faf8f8;
    padding: 5px 10px;
    text-align: left;
    word-wrap: break-word;
    width: auto;
}

.story__user-info-container2 {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    justify-content: flex-start;
}

.story__content2 {
    text-align: left;
    margin: 2px 0;
    white-space: pre-wrap;
}

.readmore-button2 {
    white-space: nowrap;
    font-weight: bolder;
    color: whitesmoke;
}

.readmore-button2:hover {
    text-decoration: underline 2px;
}

.story__username-date2 {
    margin: 0 0 0 5px;
    font-size: 14px;
    color: whitesmoke;
    font-weight: normal;
}

.story__user-name2 {
    color: whitesmoke;
    text-decoration: none;
    margin: 0 4px 0 0;
}

.story__user-name2:hover {
    text-decoration: underline 2px;
}

.story__username2 {
    margin: 0px 0px 5px 0;
}

.story__user-img2 {
    width: 50px;
    height: auto;
    border-radius: 100%;
    margin-bottom: 2px;
    cursor: pointer;
    transition: all 0.1s;
}

.story__user-img2:hover {
    filter: brightness(85%);
}

.story__user-img-container2 {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}


.story__user-info-container2 {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    justify-content: space-between;
}

.story__user-comment2 {
    margin-top: 0px;
    font-weight: bold;
    color: black;
    background-color: #faf8f8;
    padding: 5px 10px;
    border-radius: 15px 15px 15px 0;
    text-align: left;
    word-wrap: break-word;
    width: auto;
}

.story__username2 {
    margin: 0px 0px 5px 0;
}



.story__user-comment2 {
    margin-top: 0px;
    font-weight: bold;
    font-size: 14px;
    color: black;
    background-color: #faf8f8;
    padding: 5px 10px;
    border-radius: 0px 15px 15px 15px;
    text-align: left;
    word-wrap: break-word;
    width: auto;
}

.story__user-info-container2 {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    justify-content: flex-start;
}


</style>