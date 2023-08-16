<template>
    <div class="box">
        <div @click="expandInfo" class="story__expand-container user-select-none">
            <div v-if="!isExpandedInfo" class="story__user-container align-items-center">
                <div class="story__upper">
                    <h2 class="story__title "><span class="story_title highlight">CHAPTER</span><span class="story_title highlight margin-minus">{{ chapter.chapter_num }}</span></h2>
                </div> 
                <div class="story__user-img-container">
                    <span @click="navigateToUser" style="color: inherit; text-decoration: none;">
                        <img :src="imgSource" v-if="chapter.picture" alt="pic" class="story__user-img">
                    </span>
                </div> 
                <div class="story__user-info-container">
                    <div class="story__username cur-pnt"> 
                        <span @click.stop="navigateToUser" style="color: inherit; text-decoration: none;">
                            <span class="lower" style="color: whitesmoke;"><b>@</b></span><b class="story__user-name">{{ chapter.username }}</b>
                        </span>
                            <span class="story__username-date lower cur-def">· {{ chapter.created_at }} </span>
                    </div>
                </div>
            </div>
            <div v-else class="story__user-container">
                <div class="story__user-img-container-extended">
                    <span @click.stop="navigateToUser">
                        <img :src="imgSource" v-if="chapter.picture" alt="pic" class="story__user-img-extended">
                    </span>
                </div> 
                <div class="story__user-info-container-extended">
                    <div class="story__user-comment-container"><div class="story__user-comment cur-def"> {{ chapter.comment }} </div></div>
                    <div class="story__username-extended cur-pnt"> 
                        <span @click.stop="navigateToUser">
                            <span class="lower" style="color: whitesmoke;"><b>@</b></span><b class="story__user-name">{{ chapter.username }}</b>
                        </span>
                            <span class="story__username-date lower cur-def">· {{ chapter.created_at }} </span>
                    </div>
                </div>
            </div>
            <div v-if="!isExpandedInfo" class="expand-button"><div class="material-symbols-outlined expand-icon">expand_more</div></div>
            <div v-else class="expand-button margin1"><div class="material-symbols-outlined expand-icon">expand_less</div></div>
        </div>
        <article v-if="isExpandedInfo" class="story__article" :class="{ 'expanded': isExpandedInfo }">
            <div class="story__upper">
                <h2 class="story__title "><span class="story_title highlight">CHAPTER</span><span class="story_title highlight margin-minus">{{ chapter.chapter_num }}</span>{{ chapter.title.toUpperCase() }}</h2>
            </div>      
            <p class="story__content">
                {{ formatStory(chapter.content) }}
            </p>
        </article>
    </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
    setup() {
        const router = useRouter();
        return { router: router };
    },
    data() {
        return {
            isExpandedInfo: this.startExpanded
        }
    },
    props: ["chapter", "startExpanded"],
    methods: {
        formatStory(story) {
            const formattedStory = story.replace(/<br>/g, '\n')
            return formattedStory
        },
        navigateToPost() {
            this.router.push('/post/' + this.chapter._id.$oid);
        },
        navigateToUser() {
            this.router.push('/user/' + this.chapter.username);
        },
        expandInfo() {
            this.isExpandedInfo = !this.isExpandedInfo
        }
    },
    computed: {
        imgSource() {
            return require('@/assets/img/' + this.chapter.picture);
        },
        checkLength() {
            if (this.chapter.content.length >= 697) {
                return true
            }
            return false
        }
    },
    
};
</script>

<style scoped>
.margin-minus {
    margin-left: -7px;
}

.margin1 {
    margin-left: 5px;
}

.expand-button {
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
}

.story__expand-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 10px;
    cursor: pointer;
    transition: 0.3s all;
}

.story__expand-container:hover {
    background-color: rgb(50, 50, 53);
} 

.box {
    outline: rgba(255, 255, 255, 0.103) 1px solid;
    background-color: rgb(43, 43, 46);
    margin: auto 1px;
    margin-top: 1px;
    transition: 0s all;
}

.box:hover {
    outline: rgba(255, 255, 255, 0.308) 1px solid;
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
    margin: 5px 0 5px 0;
}   

.story__title {
    color: bisque;
    font-size: 17px;
    align-self: center;
    justify-self: center;
    margin: 0px 0px 0px 0px;
    font-weight: bold;
}

.story__article {
    border-radius: 2px;
    transition: all 0.2s;
    color: #d3d3d3;
    padding: 5px 10px 10px 10px;
    transition: height 1s ease;
}

.story__user-container {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
}

.story__user-comment-container {
    max-width: fit-content;
    word-wrap: break-word;
}

.story__user-comment {
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

.story__content {
    text-align: left;
    margin: 2px 0;
    white-space: pre-wrap;
}

.story__username-date {
    margin: 0 0 0 5px;
    font-size: 12px;
    color: whitesmoke;
    font-weight: normal;
    word-break: keep-all;
}

.story__user-name {
    color: whitesmoke;
    text-decoration: none;
    margin: 0 4px 0 0;
}

.story__user-name:hover {
    text-decoration: underline;
}

.story__user-img {
    width: 25px;
    height: auto;
    border-radius: 100%;
    cursor: pointer;
    transition: all 0.1s;
    margin-top: 2px;
}

.story__user-img-extended {
    width: 45px;
    height: auto;
    border-radius: 100%;
    cursor: pointer;
    transition: all 0.1s;
    margin-top: 2px;
}

.story__user-img:hover {
    filter: brightness(85%);
}

.story__user-img-extended:hover {
    filter: brightness(85%);
}

.story__user-img-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.story__user-img-container-extended {
    display: flex;
    height: 100%;
}

.story__user-info-container {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    hyphens: auto;
    justify-content: center;
    align-items: center;
}

.story__user-info-container-extended {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    hyphens: auto;
    align-items: flex-start;
}

.story__user-comment {
    margin-top: 0px;
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
    font-size: 14px;
}

.story__username-extended {
    margin: 5px 0px 0 0;
    font-size: 14px;
}
</style>