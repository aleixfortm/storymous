<template>
    <div>
        <div class="comment__user-container">
            <div><img src="../../assets/img/reply_icon3.png" alt="reply icon" style="max-width: 25px; margin: 0 0px 0 0px; transform: scaleX(-1); "></div>
            <div class="comment__user-img-container">
                <img :src="imgSource" v-if="picture" alt="Profile picture" class="comment__user-img">
            </div> 
            <div class="story__user-info-container">
                <div class="comment__username cur-pnt"> 
                    <a href="" style="color: inherit; text-decoration: none;">
                        <span class="lower"><b>@</b></span><b class="story__user-name">{{ username }}</b>
                    </a>
                        <span class="comment__username-date lower cur-def">· {{ date }}</span>
                </div>
                <div class="comment__user-comment-container"><div class="comment__user-comment cur-def">{{ content }}</div></div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {

        }
    },
    props: ["_id", "content", "username", "date", "picture"],
    components: {

    },
    methods: {

    },
    computed: {
        imgSource() {
            return require('../../assets/img/' + this.picture);
        },
    },
    
};

</script>

<style scoped>
.story__user-info-container {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    hyphens: auto;
    justify-content: space-between;
}

.comment__user-container {
    padding: 5px 0px 6px 0;
    display: flex;
    flex-direction: row;
    background-color: rgba(110, 110, 110, 0.199);
    border-radius: 10px;
    margin: 8px 0 0 0;
}

.story__user-name {
    color: whitesmoke;
    text-decoration: none;
}

.story__user-name:hover {
    text-decoration: underline;
}

#comment_content {
    width: 100%;
    height: 52px;
    color: whitesmoke;
    font-size: 14px;
    font-family: inherit;
    background-color: #445061;
    border: 2px dashed #313d4d;
    border-radius: 5px;
    padding: 5px 10px 10px 10px;
    margin: 0;
    margin-top: 4px;
    margin-bottom: 5px;
    transition: all 0.2s;
    resize: none;
    box-sizing: border-box;
}

#comment_content:focus {
    background-color: #4b5461;
    color: whitesmoke;
    border: 2px solid #313d4d;
    box-shadow: 0 0 10px 0 #37414e;
}

.comment__username {
    margin: 0px 0px 5px 0;
    color: whitesmoke;
}

.comment__user-comment-container {
    max-width: fit-content;
    word-wrap: break-word;
}

.comment__username-date {
    margin: 0 0 0 5px;
    font-size: small;
}

.comment__user-comment {
    font-weight: bold;
    font-size: 14px;
    color: black;
    background-color: #faf8f8;
    padding: 5px 10px;
    border-radius: 0 15px 15px 15px;
    text-align: left;
    word-wrap: break-word;
    hyphens: auto;
    width: auto;
    margin: 0 5px 0 0;
}

.comment__user-img-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}


.comment__user-img {
    width: 50px;
    height: auto;
    border-radius: 100%;
    border: 0px solid whitesmoke;
    margin-bottom: 2px;
    cursor: pointer;
    transition: all 0.1s;
}

.comment__user-img:hover {
  filter: brightness(85%);
}

</style>