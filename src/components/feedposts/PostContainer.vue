<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,300,1,200" />

    <div>
        <div :class="outlineClass">
            <span>
                <div class="post-top-data-container">

                    <div class="story__user-container" @click="navigateToPost">
                        <div class="story__user-img-container">
                            <span @click.stop="navigateToUser">
                                <img :src="imgSource" v-if="picture" alt="pic" class="story__user-img">
                            </span>
                        </div> 
                        <div class="story__user-info-container">
                            <div class="story__user-comment-container"><div class="story__user-comment cur-def"> {{ postComment }} </div></div>
                            <div class="story__username cur-pnt"> 
                                <span @click.stop="navigateToUser">
                                    <span class="lower" style="color: whitesmoke;"><b>@</b></span><b class="story__user-name">{{ username }}</b>
                                </span>
                                    <span class="story__username-date lower cur-def">· {{ date }} </span>
                            </div>
                        </div>
                    </div>
                </div>
                <article class="story__article" @click="navigateToPost">
                    <div class="story__upper">
                        <h2 v-if="chapterNum > 0" class="story__title "><span class="story_title highlight">CHAPTER</span><span class="story_title highlight margin-minus">{{ chapterNum }}</span>{{ title.toUpperCase() }}</h2>
                        <h2 v-else class="story__title "><span class="story_title highlight">PROLOGUE</span>{{ title.toUpperCase() }}</h2>
                    </div>
                    <div class="tag-section">
                        <post-tag v-for="tag in tags" :key="tag" :clickable="false" :tag="tag"></post-tag>
                    </div>
                    <div class="story__content">
                        <div class="story__content-text">{{ formatStory(content) }}</div>
                    </div>
                </article>
    
                <div class="story-stats user-select-none">
                    <div class="story-stats-section leaf" :class="[leavesMutable.includes(currentUser) ? 'includes-leaf' : '']" @click.prevent="increaseLeaves">
                        <span class="material-symbols-outlined margin1 leaf-icon" :class="[leavesMutable.includes(currentUser) ? 'includes-leaf-icon' : '']">
                            nest_eco_leaf
                        </span>
                        <span class="icon-text-icon-s">{{ leavesMutable.length }}&nbsp;</span><span class="icon-text-icon">Leaves</span>
                    </div>
                    <div class="story-stats-section view"><span class="material-symbols-outlined margin1 view-icon">bar_chart</span><span class="icon-text-icon">{{ views }} Views</span></div>
                    <div class="story-stats-section comment"><span class="material-symbols-outlined margin1 comment-icon">chat</span><span class="icon-text-icon">{{ comments.length }} Comments</span></div>
                </div>
            </span>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { mapActions } from "vuex";
import { useRouter } from 'vue-router';
import { API_BASE_URL } from '@/config';
import axios from 'axios';

import PostTag from "@/components/UIcomponents/PostTag.vue"

export default {
    components: {
        PostTag,
    },
    data() {
        return {
            leavesMutable: this.leaves,
            executed: false
        }
    },
    setup() {
        const router = useRouter();
        return { router: router };
    },
    props: ["_id", "title", "content", "username", "postComment", "date", "picture", "color", "views", "feedMode", "tags", "leaves", "chapterNum", "story_name", "comments"],
    methods: {
        ...mapActions('message', ['setLoginError']),
        formatStory(story) {
            const formattedStory = story.replace(/<br>/g, '\n')
            if (formattedStory.length > 700 && this.feedMode) {
                return formattedStory.substring(0, 700);
            }
            return formattedStory
        },
        navigateToPost() {
            this.router.push('/chapter/' + this._id.$oid);
        },
        navigateToUser() {
            this.router.push('/user/' + this.username);
        },
        increaseLeaves() {
            if (this.isLoggedIn) {
                const data_packet = {
                    chapter_id: this._id.$oid,
                    username: this.currentUser,
                    username_receiver: this.username
                }
                if (!this.executed) {
                    if (!this.leavesMutable.includes(this.currentUser)) { // leaves array does not include currentUser
                        this.leavesMutable.push(this.currentUser)
                        
                        axios
                            .post(`${API_BASE_URL}/add_leaf_chapter`, data_packet)
                            .catch(error => {
                                console.log(error);
                            });
                    } else { //if array does include currentUser
                        const index = this.leavesMutable.indexOf(this.currentUser);
                        if (index !== -1) {
                            this.leavesMutable.splice(index, 1);
                        }
                        axios
                            .post(`${API_BASE_URL}/remove_leaf_chapter`, data_packet)
                            .catch(error => {
                                console.log(error);
                            });
                    }
                    this.executed = true;

                } else { //executes if is logged in but has already made an API call
                    if (!this.leavesMutable.includes(this.currentUser)) { // leaves array does not include currentUser
                        this.leavesMutable.push(this.currentUser)
                    } else {
                        const index = this.leavesMutable.indexOf(this.currentUser);
                        if (index !== -1) {
                            this.leavesMutable.splice(index, 1);
                        }
                    }
                }
            } else {
                this.setLoginError()
            }
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched"]),
        imgSource() {
            return require('@/assets/img/' + this.picture);
        },
        outlineClass() {
            return `outline ${this.color}`;
        },
        checkLength() {
            if (this.content.length >= 697) {
                return true
            }
            return false
        },
    }
};
</script>

<style scoped>

.icon-text-icon {
    font-size: 15px;
    color: rgb(187, 187, 187);
}

.icon-text-icon-s {
    font-size: 15px;
}

.margin-minus {
    margin-left: -7px;
}

.material-symbols-outlined {
  font-size: 20px;
  font-variation-settings:
  'FILL' 1,
  'wght' 400,
  'GRAD' 200,
  'opsz' 48
}

.leaf {
    color: white;
    transition: all 0.1s;
}

.leaf-icon {
    color: rgb(187, 187, 187);
}

.leaf:hover .leaf-icon{
    color: rgb(0, 255, 76);
}

.includes-leaf {
    color: rgb(0, 255, 106);
}

.includes-leaf-icon {
    color: rgb(0, 255, 106);
}

.view {
    color: rgb(187, 187, 187);
    transition: all 0.1s;
}

.view:hover .view-icon{
    color: rgb(0, 183, 255);
}

.comment {
    color: rgb(187, 187, 187);
    transition: all 0.1s;

}

.comment-icon {
    font-size: 17px;
}

.comment:hover .comment-icon {
    color: rgb(255, 255, 108);
}

.share {
    color: white;
    transition: all 0.1s;
}

.share:hover .share-icon {
    color: rgb(255, 109, 255);
}


.margin1 {
    margin-right: 2px;
}

.margin2 {
    margin-right: 5px;
}

.user-out {
    padding: 5px 5px 0 5px;
}

.separator {
    border-top: rgba(245, 245, 245, 0.075) 1px solid;
    width: 95%;
    margin: auto;
}

.story-stats {
    display: flex;
    color: whitesmoke;
    margin: 0px;
    justify-content: flex-start;
    height: 30px;
    width: 100%;
    transition: 0.1s all;
}

.story-stats-section {
    display: flex;
    align-items: center;
    font-size: 13px;
    font-family: monospace;
    padding: 2px 12px 2px 6px;
}

.story-stats-section:hover {
    background-color: rgba(194, 194, 194, 0.137);
    border-radius: 1px;
}

.tag-section {
    display: flex;
    justify-content: left;
    margin: 7px 0 0px 0;
    flex-wrap: wrap;
}

.highlight {
    background-color: bisque;
    color: black;
    border-radius: 2px;
    padding: 0px 2px;
    margin-right: 10px;
    font-size: 16px;
}

.story__upper {
    display: flex;
    margin: 2px 0 5px 0;

}   

.story__title {
    color: bisque;
    font-size: 16px;
    align-self: center;
    justify-self: center;
    margin: 0px 0px 0px 0px;
    font-weight: bold;
}

.origin {
    background-color: rgba(215, 215, 215, 0.062);
    color: rgb(255, 255, 255);
    font-size: 13px;
    padding: 0px 3px;
    border-radius: 1px;
    width: fit-content;
}

.origin-container {
    display: flex;
    justify-content: flex-start;
}

.story__article {
    padding: 4px 10px 5px 10px;
    border-radius: 2px;
    cursor: pointer;
    transition: all 0s;

    color: #d3d3d3
}

.post-top-data-container {
    padding: 5px 10px 0 10px;
    background-color: rgba(148, 148, 148, 0.103);
    border-radius: 3px 3px 0 0;
    transition: 0.3s all;
}

.post-top-data-container:hover {
    background-color: rgba(143, 143, 143, 0.062);
}

.post-top-data-container.salmon {
    background-color: rgba(112, 47, 40, 0.863);
}

.post-top-data-container.red {
    border: 4px rgb(255, 25, 0) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 25, 0);
}

.post-top-data-container.blue {
    background-color: rgba(0, 123, 206, 0.377);
}

.post-top-data-container.green {
    border: 4px rgb(55, 182, 97) solid;
    box-shadow: 0px 0px 5px 2px rgb(55, 182, 97);
}

.post-top-data-container.yellow {
    border: 4px rgb(255, 217, 0) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 217, 0);
}

.post-top-data-container.white {
    border: 4px rgb(255, 255, 255) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 255, 255);
}

.post-top-data-container.purple {
    border: 4px rgb(183, 0, 255) solid;
    box-shadow: 0px 0px 5px 2px rgb(183, 0, 255);
}

.post-top-data-container.pink {
    border: 4px rgb(255, 0, 179) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 0, 179);
}

.post-top-data-container.orange {
    border: 4px rgb(255, 145, 0) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 145, 0);
}


.outline {
    margin-top: 12px;
    /*padding: 5px 4px 4px 4px;*/
    height: fit-content;
    width: 100%;
    border-radius: 5px;
    border: 1px rgba(255, 255, 255, 0.151) solid;
    background-color: rgba(60, 60, 63, 0.425);
    background-color: rgba(37, 37, 39, 0.425);
    background-color: rgba(52, 52, 54, 0.425);
    background-color: rgba(39, 39, 39, 0.788);
    font-family: inherit;
    transition: 0.2s all;
}

.outline:hover {
    border: 1px rgb(190, 190, 190) solid;
    cursor: pointer;
}

.story__user-container {
    display: flex;
    flex-direction: row;
    padding: 2px 0px 0px 0;
}

.story__user-img-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.story__user-comment-container {
    max-width: fit-content;
    word-wrap: break-word;
}


.story__user-info-container {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: 100%;
    hyphens: auto;
    justify-content: space-between;
}

.story__title-container {
    background-color: rgb(255, 214, 164);
    padding: 2px;
    justify-content: left;
    border-radius: 5px;
    margin-bottom: 8px;
    width: 100%;
    word-wrap: break-word;
    hyphens: auto;
}


.story__content {
    -webkit-mask-image: linear-gradient(0deg, transparent, white 80%);
}

.story__content-text {
  text-align: left;
  margin: 2px 0;
  font-family: monospace;
  font-size: 15px;
  white-space: pre-wrap;

}

.readmore-button {
    white-space: nowrap;
    font-weight: bolder;
    color: #dddddd;
}

.readmore-button:hover {
    text-decoration: underline;
}

.story__username-date {
    margin: 0 0 0 5px;
    font-size: 13px;
    color: rgba(245, 245, 245, 0.774);
    font-weight: normal;
}

.story__user-name {
    color: whitesmoke;
    text-decoration: none;
    margin: 0 4px 0 0;
}

.story__user-name:hover {
    text-decoration: underline;
}

.story__username {
    margin: 5px 0px;
    font-size: 14px;
}

.story__user-img {
    width: 45px;
    height: auto;
    border-radius: 100%;
    margin-bottom: 5px;
    cursor: pointer;
    transition: all 0.2s;
}

.story__user-img:hover {
    filter: brightness(85%);
}

.story__user-img-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.post__story {
    box-shadow: 0 0 10px 0 #3c4755;
    margin-bottom: 10px;
}

.story__user-info-container {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    hyphens: auto;
    justify-content: space-between;
}

.story__user-comment {
    margin-top: 0px;
    font-size: 15px;
    font-weight: bold;
    color: black;
    background-color: #faf8f8;
    padding: 3px 10px;
    border-radius: 15px 15px 15px 0;
    text-align: left;
    word-wrap: break-word;
    hyphens: auto;
    width: auto;
}

.story__username {
    margin: 5px 0px;
}

.story__user-tags {
    margin-top: 8px;
    display: flex;
    flex-direction: row;
}

.story__tag {
    border-radius: 15px;
    padding: 1px 8px;
    color: white;
    opacity: 0.8;
    margin-right: 5px;
}

.post-icons-bar {
    display: flex;
    justify-content: right;
    font-size: 13px;
    height: fit-content
}

.post-icon-bg {
    height: fit-content;
    padding: 0 4px;
    display: flex;
    background-color: rgba(43, 43, 46, 0.671);
    border-radius: 10px;
    opacity: 1;
}

.post-icon-bg:hover {
    cursor: pointer;
    display: flex;
    background-color: rgba(43, 43, 46, 0.671);
    border-radius: 12px;
}


.post-icons {
    background-color: rgba(43, 43, 46, 0.671);
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