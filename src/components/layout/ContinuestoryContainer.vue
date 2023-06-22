<template>
    <div class="background-story-reply2">
        <router-link to="" @click="navigateToPost" style="text-decoration: none;" >
            <div class="story__user-container2">
                <div class="sum-icon-container2">
                    <img src="../../assets/img/plus_icon4.png" alt="Plus icon" class="sum-icon2">
                </div>
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
            <article class="story__article2">  
                <p class="story__content2">
                    {{ formatStory(content) }}
                    <b class="readmore-button2"><em>Read more</em></b>
                </p>
            </article>
        </router-link>
    </div>
</template>

<script>
import { useRouter } from 'vue-router';
import { mapActions } from "vuex";

export default {
    data() {
        return {
            outlineColors: ["red", "blue", "green", "yellow", "white", "purple", "pink", "orange", "salmon"]
        }
    },
    setup() {
        const router = useRouter();
        return { router: router };
    },
    props: ["_id", "content", "username", "postComment", "date", "imgName"],
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
                imgName: this.imgName
            };
            this.emitData(dataToEmit);
            this.router.push('/storymous/post/' + this._id.$oid);
        },
        navigateToUser() {
            this.router.push('/storymous/user/' + this.username);
        }
    },
    computed: {
        imgSource() {
            return require('../../assets/img/' + this.imgName);
        },
    },
};
</script>

<style scoped>
.sum-icon-container2 {
    margin: 0 5px 0 0;
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
}

.origin2 {
    background-color: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
    font-size: 14px;
    padding: 1px 4px;
    border-radius: 3px;
    width: fit-content;
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.568);
}

.origin-container2 {
    display: flex;
    justify-content: flex-start;
    margin: 2px 0 0 0;
}

.outline2 {
    margin-top: 20px;
    padding: 5px 10px 10px 10px;
    height: fit-content;
    width: 100%;
    /*border: 2px whitesmoke dashed;*/
    border-radius: 5px;
    border: 2px rgb(55, 182, 97) solid;
    background-color: rgba(60, 134, 85, 0.103);
}

.outline.salmon2 {
    border: 2px rgb(255, 109, 93) solid;
    background-color: rgba(255, 109, 93, 0.123);
}

.outline.red2 {
    border: 2px rgb(255, 25, 0) solid;
    background-color: rgba(255, 25, 0, 0.11);
}

.outline.blue2 {
    border: 2px rgb(0, 153, 255) solid;
    background-color: rgba(0, 153, 255, 0.103);
}

.outline.green2 {
    border: 2px rgb(55, 182, 97) solid;
    background-color: rgba(60, 134, 85, 0.103);
}


.story__article2 {
    padding: 10px 15px;
    border-radius: 2px;
    cursor: pointer;
    transition: all 0s;
    background-color: rgb(46, 46, 53);
    color: rgb(223, 223, 223);
    font-weight: 400;
}


.story__user-container2 {
    padding: 2px 10px 2px 2px;
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
    border-radius: 15px 15px 15px 15px;
    text-align: left;
    word-wrap: break-word;
    hyphens: auto;
    width: auto;
}

.story__user-info-container2 {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: -moz-fit-content;
    width: fit-content;
    -webkit-hyphens: auto;
    hyphens: auto;
    justify-content: space-between;
}


.story__upper2 {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 0px 0px;
    width: 100%;
}

.story__title-container2 {
    background-color: rgb(255, 214, 164);
    padding: 2px;
    justify-content: left;
    border-radius: 5px;
    margin-bottom: 8px;
    width: 100%;
    word-wrap: break-word;
    hyphens: auto;
}

.story__title2 {
    padding: 2px 8px;
    border-radius: 5px;
    color: #2d3441;
    margin: 0px 0px;
    font-size: large;
    word-wrap: break-word;
    hyphens: auto;
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
    width: 55px;
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

.post__story2 {
    box-shadow: 0 0 10px 0 #3c4755;
    margin-bottom: 10px;
}

.story__user-info-container2 {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    hyphens: auto;
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
    hyphens: auto;
    width: auto;
}

.story__username2 {
    margin: 5px 0px;
}

.story__user-tags2 {
    margin-top: 8px;
    display: flex;
    flex-direction: row;
}

.story__tag2 {
    border-radius: 15px;
    padding: 1px 8px;
    color: white;
    opacity: 0.8;
    margin-right: 5px;
}

.post-icons-bar2 {
    display: flex;
    justify-content: right;
    font-size: 13px;
    height: fit-content
}

.post-icon-bg2 {
    height: fit-content;
    padding: 0 4px;
    display: flex;
    background-color: rgba(240, 248, 255, 0);
    border-radius: 10px;
    opacity: 1;
}

.post-icon-bg2:hover {
    cursor: pointer;
    display: flex;
    background-color: rgba(240, 248, 255, 0.219);
    border-radius: 12px;
}


.post-icons2 {
    background-color: #31394600;
    margin: 5px 0 0px 0;
    padding: 2px 4px 0px 5px;
    /*border-radius: 5px;*/
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    width: fit-content;
    height: fit-content;
    align-items: center;
}

</style>