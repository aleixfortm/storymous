<template>
    <div class="background-story-reply2">
        <span @click="navigateToPost" style="text-decoration: none;" >
            <div class="story__user-container2">
                <div class="sum-icon-container2">
                    <img src="@/assets/img/plus_icon4.png" alt="Plus icon" class="sum-icon2">
                </div>
                <div class="story__user-img-container2">
                    <span @click.stop="navigateToUser" style="color: inherit; text-decoration: none;">
                        <img :src="imgSource" alt="pic" class="story__user-img2">
                    </span>
                </div> 
                <div class="story__user-info-container2">
                    <div class="story__username2 cur-pnt"> 
                        <span @click.stop="navigateToUser" style="color: inherit; text-decoration: none;">
                            <span class="lower" style="color: whitesmoke;"><b>@</b></span><b class="story__user-name2">{{ chapter.username }}</b>
                        </span>
                            <span class="story__username-date2 lower cur-def">· {{ chapter.created_at }} </span>
                    </div>
                    <div class="story__user-comment-container2"><div class="story__user-comment2 cur-def"> {{ chapter.comment }} </div></div>
                </div>
            </div>
            <article class="story__article2">
                <div class="story__upper">
                    <h2 class="story__title "><span class="story_title highlight">CHAPTER</span><span class="story_title highlight margin-minus">{{ chapter.chapter_num }}</span>{{ chapter.title.toUpperCase() }}</h2>
                </div>
                <template v-if="isExtendable">
                    <p v-if="!isExtended" class="story__content2">
                        {{ formatStory(chapter.content).substring(0, 170) + '...' }}
                        <br>
                        <span @click.stop="extend" class="readmore">Read more</span>
                    </p>
                    <p v-else class="story__content2">
                        {{ formatStory(chapter.content) }}
                    </p>
                </template>
            </article>
        </span>
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
    data() {
        return {
            isExtendable: true,
            isExtended: false
        }
    },
    props: ["chapter"],
    methods: {
        formatStory(story) {
            story = story.replace(/<br>/g, '\n');
            if (story.length > 300) {
                return story
            }
            return story
        },
        ...mapActions("emitdata", ["emitData"]),
        /*
        navigateToPost() {
            const dataToEmit =  {
                _id: this.chapter._id,
                content: this.chapter.content,
                username: this.chapter.username,
                postComment: this.chapter.postComment,
                date: this.chapter.date,
                picture: this.chapter.picture
            };
            this.emitData(dataToEmit);
            this.router.push('/chapter/' + this.chapter._id.$oid);
        },
        */
        navigateToPost() {
            console.log(this.chapter._id)
            this.$emit("selected-chapter", this.chapter._id);
        },
        navigateToUser() {
            this.router.push('/user/' + this.chapter.username);
        },
        extend() {
            this.isExtended = true
        }
    },
    computed: {
        imgSource() {
            return require('@/assets/img/' + this.chapter.picture);
        },
    },
};
</script>

<style scoped>
.margin-minus {
    margin-left: -7px;
}

.readmore {
    font-weight: bold;
    font-style: italic;
}
.readmore:hover {
    text-decoration: underline;
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

.sum-icon-container2 {
    margin: 5px 3px 0 0;
}

.sum-icon2{
    max-width: 16px;
    margin: 0px;
}

.background-story-reply2 {
    background-color: rgb(46, 46, 53);
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
    color: #d3d3d3;
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
    justify-content: flex-start;

}

.story__user-comment-container2 {
    max-width: fit-content;
    word-wrap: break-word;

}

.story__content2 {
    text-align: left;
    margin: 2px 0;
    white-space: pre-wrap;
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
    text-decoration: underline;
}

.story__user-img2 {
    width: 45px;
    height: auto;
    border-radius: 100%;
    margin-bottom: 2px;
    cursor: pointer;
    transition: all 0.1s;
}

.story__user-img2:hover {
    filter: brightness(85%);
}

.story__user-comment2 {
    font-weight: bold;
    color: black;
    background-color: #faf8f8;
    padding: 3px 10px;
    border-radius: 0px 15px 15px 15px;
    text-align: left;
    word-wrap: break-word;
    width: auto;
    font-size: 15px;
    margin: 2px 5px 0 0;
}

.story__username2 {
    margin: 0px 0px 1px 0;
}

.story__user-info-container2 {
    display: flex;
    flex-direction: column;
    margin: 0 0 0px 5px;
    width: fit-content;
    justify-content: space-between;
}
</style>