<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,300,1,200" />

    <div>
        <div :class="outlineClass">
            <span>
                <div class="origin-container" @click="navigateToPost">
                    <div class="origin">Started "<span style="font-weight: bold;">{{ title }}</span>"</div>
                </div>
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
                <div class="separator"></div>
                <article class="story__article" @click="navigateToPost">
                    <div class="story__upper">
                        <h2 class="story__title "><span class="story_title highlight">CHAPTER</span><span class="story_title highlight margin-minus">{{ chapterNum }}</span>{{ title.toUpperCase() }}</h2>
                    </div>
                    <div class="tag-section">
                        <post-tag v-for="tag in tags" :key="tag" :clickable="false" :tag="tag"></post-tag>
                    </div>
                    <p class="story__content">
                        {{ formatStory(content) }}
                        <b v-if="feedMode && checkLength" class="readmore-button"><em>Read more</em></b>
                    </p>
                </article>
                <div class="separator"></div>
                <div class="story-stats user-select-none">
                    <div class="story-stats-section leaf" :class="[leavesMutable.includes(currentUser) ? 'includes-leaf' : '']" @click.prevent="increaseLeaves">
                        <span class="material-symbols-outlined margin1 leaf-icon" :class="[leavesMutable.includes(currentUser) ? 'includes-leaf-icon' : '']">
                            nest_eco_leaf
                        </span>
                        {{ leavesMutable.length }}
                    </div>
                    <div class="story-stats-section view"><span class="material-symbols-outlined margin1 view-icon">bar_chart</span>{{ views }}</div>
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
    props: ["_id", "title", "content", "username", "postComment", "date", "picture", "color", "views", "feedMode", "tags", "leaves", "chapterNum"],
    methods: {
        ...mapActions('message', ['setLoginError']),
        formatStory(story) {
            const formattedStory = story.replace(/<br>/g, '\n')
            if (formattedStory.length > 700 && this.feedMode) {
                return formattedStory.substring(0, 700) + '...';
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
                    post_id: this._id.$oid,
                    username: this.currentUser,
                    username_receiver: this.username
                }
                if (!this.executed) {
                    if (!this.leavesMutable.includes(this.currentUser)) { // leaves array does not include currentUser
                        this.leavesMutable.push(this.currentUser)
                        
                        axios
                            .post(`${API_BASE_URL}/add_leaves_chapter`, data_packet)
                            .catch(error => {
                                console.log(error);
                            });
                    } else { //if array does include currentUser
                        const index = this.leavesMutable.indexOf(this.currentUser);
                        if (index !== -1) {
                            this.leavesMutable.splice(index, 1);
                        }
                        axios
                            .post(`${API_BASE_URL}/remove_leaves_chapter`, data_packet)
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
.margin-minus {
    margin-left: -7px;
}

.material-symbols-outlined {
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
    color: white;
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
    color: white;
    transition: all 0.1s;
}

.view:hover .view-icon{
    color: rgb(131, 189, 255);
}

.comment {
    color: white;
    transition: all 0.1s;
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
    margin: 5px 0 2px 5px;
    justify-content: center;
}

.story-stats-section {
    display: flex;
    align-items: center;
    margin: 0 12px;
    padding: 1px 6px 1px 1px;
}

.story-stats-section:hover {
    background-color: rgba(194, 194, 194, 0.137);
    border-radius: 10px;
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
    padding: 0 3px;
    margin-right: 10px;
    font-size: 17px;
}

.story__upper {
    display: flex;
    margin: 2px 0 5px 0;

}   

.story__title {
    color: bisque;
    font-size: 17px;
    align-self: center;
    justify-self: center;
    margin: 0px 0px 0px 0px;
    font-weight: bold;
}

.origin {
    background-color: rgba(160, 160, 160, 0.247);
    color: rgb(255, 255, 255);
    font-size: 14px;
    padding: 0px 3px;
    border-radius: 1px;
    width: fit-content;
    box-shadow: 0px 0px 2px rgba(128, 128, 128, 0.568);
}

.origin-container {
    display: flex;
    justify-content: flex-start;
    margin: 2px 5px 0 5px;
}

.story__article {
    padding: 5px 10px 5px 10px;
    border-radius: 2px;
    cursor: pointer;
    transition: all 0s;
    background-color: rgb(43, 43, 46);
    color: #d3d3d3
}

.outline {
    margin-top: 12px;
    padding: 5px 4px 4px 4px;
    height: fit-content;
    width: 100%;
    border-radius: 1px;
    border: 1px rgba(255, 255, 255, 0.247) solid;
    background-color: rgb(43, 43, 46);
    transition: 0.2s all;
}

.outline:hover {
    border: 1px rgb(190, 190, 190) solid;
    cursor: pointer;
}

.story__user-container {
    padding: 10px 5px 3px 5px;
    display: flex;
    flex-direction: row;
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
    width: fit-content;
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
    text-align: left;
    margin: 2px 0;
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
    font-size: 14px;
    color: whitesmoke;
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
    background-color: rgba(240, 248, 255, 0);
    border-radius: 10px;
    opacity: 1;
}

.post-icon-bg:hover {
    cursor: pointer;
    display: flex;
    background-color: rgba(240, 248, 255, 0.219);
    border-radius: 12px;
}


.post-icons {
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