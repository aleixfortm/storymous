<template>
    <feed-container>
        <div>
            <div class="story__user-container">
                <div class="story__user-img-container">
                    <a href="" style="color: inherit; text-decoration: none;">
                        <img src="../../assets/img/default_blue.png" alt="pic" class="story__user-img">
                    </a>
                </div> 
                <div class="story__user-info-container">
                    <div class="story__user-comment-container"><div class="story__user-comment cur-def"> Viva españa viva el rey viva el orden y la ley </div></div>
                    <div class="story__username cur-pnt"> 
                        <a href="" style="color: inherit; text-decoration: none;">
                            <span class="lower"><b>@</b></span><b class="story__user-name">username</b>
                        </a>
                            <span class="story__username-date lower cur-def">date</span>
                        
                    </div>
                </div>
            </div>
            <a href="" style="color: inherit; text-decoration: none;">
                <article class="story__article">    
                    <div class="story__upper">
                        <div class="story__title-container">
                            <h2 class="story__title"> this is a long title to test </h2>
                        </div>
                    </div>
                    <p class="story__content">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab provident fugiat accusantium dolorum mollitia distinctio inventore perferendis, alias voluptatem reprehenderit adipisci molestias maiores dolor ratione qui aspernatur quisquam? Officia, quos!
                        <b class="readmore-button"><em>Read more</em></b>

                    </p>
                </article>
            </a>
        </div>
        <!--
        <span class="title">{{ title }}</span>
        <p class="content">{{ content }}</p>
        -->
    </feed-container>

</template>

<script>
import FeedContainer from "./FeedContainer.vue";

export default {
    data() {

    },
    components: {
        FeedContainer
    },
    props: ["title", "content"]
}

</script>

<style scoped>
.story__user-container {
    padding: 10px 10px;
    display: flex;
    flex-direction: row;
}

.comment__user-container {
    padding: 6px 0px;
    display: flex;
    flex-direction: row;
    margin-left: 0px;
    margin-top: 5px;
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
    margin: 6px 0px 7px 0;
}

.content-form__box {
    padding: 0 0 0 0;
    align-items: end;
    margin: 0;
}

#comment_submit {
    max-width: fit-content;
    text-align: center;
    padding-right: 10px;
    margin: 5px 0 0 0;
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
    margin-top: 0px;
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
}

.story__user-img-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.comment__user-img-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
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

.story__user-info-container {
    display: flex;
    flex-direction: column;
    margin: 0 0 0 5px;
    width: fit-content;
    hyphens: auto;
    justify-content: space-between;
}

.story__article {
    padding: 10px 15px;
    border: 2px dashed #313d4d;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0s;
}

.story__upper {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 0px 0px;
    width: 100%;
}

.story__title-container {
    background-color: bisque;
    padding: 2px;
    justify-content: left;
    border-radius: 5px;
    margin-bottom: 8px;
    width: 100%;
    word-wrap: break-word;
    hyphens: auto;
}

.story__title {
    padding: 2px 8px;
    border-radius: 5px;
    color: #2d3441;
    margin: 0px 0px;
    font-size: large;
    word-wrap: break-word;
    hyphens: auto;
}

.story__content {
    text-align: left;
    margin: 2px 0;
}

.readmore-button {
    white-space: nowrap;
    font-weight: bolder;
    color: rgb(197, 190, 207);
}

.story__username-date {
    margin: 0 0 0 0px;
    font-size: 14px;
}

.story__user-name {
    color: whitesmoke;
    text-decoration: none;
}

.story__username {
    margin: 5px 0px;
}

.story__user-img {
    width: 55px;
    height: auto;
    border-radius: 100%;
    border: 2px solid whitesmoke;
    margin-bottom: 2px;
}

.story__user-img-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.post__story {
    border: 2px solid #29313b;
    box-shadow: 0 0 10px 0 #3c4755;
    margin-bottom: 10px;
}

.story__user-img {
    width: 55px;
    height: auto;
    border-radius: 100%;
    border: 2px solid whitesmoke;
    margin-bottom: 2px;
}

.comment__user-img {
    width: 45px;
    height: auto;
    border-radius: 100%;
    border: 1.5px solid whitesmoke;
    margin-bottom: 2px;
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