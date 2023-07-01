<template>
    <feed-container v-if="isLoggedIn">
        <img src="../assets/img/storymous-forest-min.png" alt="storymous forest" class="testimage">
        <!--
        <div class="loggedintop">
            <div class="loggedimagecontainer">
                <img src="../assets/img/tree2.jpeg" alt="storymous tree" class="treeimg">
            </div>
            <div class="statstop">
                <div class="statstop1">
                    The <b style="color: greenyellow;">story tree</b> holds a total of <b>122</b> <b><span style="color: rgb(240, 150, 15);">stories</span></b> from <b>21</b><b> <span style="color: rgb(30, 153, 210);"> authors</span></b>
                </div>
                <div class="statstop1">
                    <b>84</b><b><span style="color: rgb(255, 0, 106);"> readers</span></b> have been spotted nearby
                </div>
                <div class="statstop2">
                    <b>2</b> new  <b><span style="color: rgb(240, 150, 15);">stories</span></b> published today
                </div>
            </div>
        </div>
        -->
        <div class="create_newstory">
            <img class="postimage" v-if="userFetchedPicture" :src="imgSource" alt="profilepic">
            <router-link to="" class="story_form">
                <input type="text" placeholder="Write new story" @click="navigateToNewPost">
            </router-link>
        </div>
    </feed-container>
    <feed-container v-else class="homepage-top">
        <div class="welcome-message" v-if="!loggedOutLoading">
            <div class="messagecontainer">
                <div class="innermessagecontainer">
                    Welcome to  <b>Storymous</b>! <br>
                    <span class="innermessagecontainer2">Amazing stories await...</span>
                </div>
            </div>
            <div class="imagecontainer">
                <img class="welcomeimage" src="../assets/img/astronaut_reading.jpeg" alt="astronaut reading under tree">
            </div>
        </div>
    </feed-container>
    <div v-if="isLoggedIn" class="block">
        <div class="rectangle">
            <select-button @click="setSelectedTab('latest-feed')" :mode="selectedTab === 'following-feed' ? null : 'flat'">
                <div>Latest</div>
            </select-button>
        </div>
        <div class="rectangle">
            <select-button @click="setSelectedTab('following-feed')" :mode="selectedTab === 'following-feed' ? 'flat' : null">
                <div>Following</div>
            </select-button>
        </div>
    </div>
    <div v-else class="block">

        <div class="rectangle">
            <select-button @click="setSelectedTab('latest-feed')" :mode="selectedTab === 'following-feed' ? null : 'flat'">
                <div>Explore</div>
            </select-button>
        </div>
    </div>

    <component :is="selectedTab" :posts="posts" :loading="loading"></component>

</template>


<script>
import { mapGetters } from 'vuex';
import { useRouter } from 'vue-router';
import { API_BASE_URL } from '../config';

import axios from 'axios';

import FeedContainer from "../components/layout/FeedContainer.vue"
import SelectButton from "../components/SelectButton.vue";
import LatestFeed from "../pages/subpages/LatestFeed.vue";
import FollowingFeed from "../pages/subpages/FollowingFeed.vue";

export default {
    components: {
        FeedContainer,
        SelectButton,
        LatestFeed,
        FollowingFeed
    },
    setup() {
        const router = useRouter();
        return { router: router };
    },
    data() {
        return {
            posts: {},
            selectedTab: 'latest-feed',
            openDialog: true,
            userLogged: true,
            text: " ",
            showCharacter: true,
            loading: true,
            loggedOutLoading: false,
            loggedOutImageLoaded: false
        }
    },
    mounted() {
    if (this.isLoggedIn) {
        console.log(this.currentUser)
        axios
            .get(`${API_BASE_URL}/homepage_posts/${this.currentUser}`)
            .then(response => {
                this.posts = response.data;
                this.loading = false;
                this.loggedOutLoading = false;
            })
            .catch(error => {
                console.log(error);
            });
    } else {
        axios
            .get(`${API_BASE_URL}/posts`)
            .then(response => {
                this.posts = response.data;
                this.loading = false;
                this.loggedOutLoading = false;
            })
            .catch(error => {
                console.log(error);
            });
    }
    
    },
    methods: {
        setSelectedTab(tab) {
            this.selectedTab = tab;
        },
        navigateToNewPost() {
            this.router.push('/newpost');
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched"]),
        modifiedText() {
            if (this.showCharacter) {
                return ""; // Replace character with underscore when showCharacter is false
            } else {
                return ""
            }
        },
        imgSource() {
            return require("../assets/img/" + this.userFetchedPicture);
        },
    }
}
</script>


<style scoped>
.testimage {
    width: 100%;
    border-radius: 10px;
    opacity: 1;
}

.statstop {
    color: whitesmoke;
    padding: 10px;
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: 0px 0 0 20px;
    
}

.statstop1{
    margin: 0 0 10px 0;
    background-color: rgba(153, 153, 153, 0.19);
    padding: 5px;
    border-radius: 10px;
    cursor: pointer;
    font-size: large;
    transition: all 0.1s;
}

.statstop1:hover {
    background-color: rgba(134, 134, 134, 0.151);
}

.statstop2 {
    margin: 0 0 0 0;
    background-color: rgba(153, 153, 153, 0.19);
    padding: 5px;
    border-radius: 10px;
    cursor: pointer;
    font-size: large;
    transition: all 0.1s;
}

.statstop2:hover {
    background-color: rgba(134, 134, 134, 0.151);
}

.loggedintop {
    background-color: rgb(119 119 119 / 19%);
    padding: 5px;
    border-radius: 10px;
    display: flex;
    align-items: center;
}

.loggedimagecontainer {
    width: 300px;
    height: auto;
    align-self: center;
}

.treeimg {
    width: 100%;
    border-radius: 40px;
}

@media (max-width: 500px) {
    .statstop {
        color: whitesmoke;
        padding: 10px;
        width: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin: 0px 0 0 5px;
    }

    .statstop1 {
    font-size: medium;
}

.statstop2 {
    margin: 0 0 10px 0;
    background-color: rgba(153, 153, 153, 0.19);
    padding: 5px;
    border-radius: 10px;
    cursor: pointer;
    font-size: medium;
}
    
    .loggedimagecontainer {
    width: 200px;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
}
.loggedintop {
    background-color: rgb(119 119 119 / 19%);
    padding: 5px;
    border-radius: 10px;
    display: flex;
    justify-content: center;
}
}

.homepage-top {
    /*background-color: rgba(90, 90, 90, 0.13);*/
    padding: 20px 10px;
    border-radius: 10px;
}

.messagecontainer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: left;
    position: absolute;
    margin: 95px 140px 0 0;
}



.innermessagecontainer {
    width: auto; /*360px*/
    margin: 0 20px 100px 0;
    background-color: white;
    padding: 10px 20px 10px 25px;
    border-radius: 40px 40px 0 40px;
    font-size: x-large;
    font-weight: bold;
    cursor: default;
    animation: floatAnimation 4s ease-in-out infinite;
}

.innermessagecontainer2 {
    font-size: large;
}

@keyframes floatAnimation {
  0% {
    transform: translateY(-5px);
  }
  50% {
    transform: translateY(5px);
  }
  100% {
    transform: translateY(-5px);
  }
}

.welcome-message {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    margin: 0 80px 0 0;
}

.welcomeimage {
    height: auto;
    width: 100%;
    border-radius: 300px;
    max-width: 300px;
    align-self: flex-end;
}

.imagecontainer {
    width: fit-content;
    display: flex
}

@media (max-width: 690px) {
  .responsive-text {
    font-size: 16px; /* Adjusted font size for smaller screens */
  }

  .innermessagecontainer {
    margin: 0 120px -86px 10px;
    width: auto; /*360px*/
    background-color: white;
    padding: 10px 20px 10px 20px;
    border-radius: 20px 20px 0 20px;
    font-size: large;
    font-weight: bold;
    cursor: default;

}

.innermessagecontainer2 {
    font-size: medium;
}

.welcome-message {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: auto;
}
}



@media (max-width: 565px) {
  .responsive-text {
    font-size: 14px; /* Further adjusted font size for even smaller screens */
  }

  .innermessagecontainer {
    width: auto; /*360px*/
    background-color: white;
    padding: 10px 20px 10px 20px;
    border-radius: 20px 20px 0 20px;
    font-size: medium;
    font-weight: bold;
    cursor: default;
}

.innermessagecontainer2 {
    font-size: small;
}

.welcome-message {
    display: flex;
    flex-direction: row;
    justify-content: center;
}
}

@media (max-width: 520px) {
    .messagecontainer {
        max-width: 180px;
    }
  .innermessagecontainer {
    margin: -25px 10px 50px 10px;
    width: auto; /*360px*/
    background-color: white;
    padding: 10px 20px 10px 20px;
    border-radius: 20px 20px 0 20px;
    font-size: medium;
    font-weight: bold;
    cursor: default;
}

.innermessagecontainer2 {
    font-size: small;
}
}
/*

*/

.story_form {
    width: 100%;
    cursor: default;
}

form {
    display: block;
    width: 90%;
    margin: 0 20px 0 0;
}

input[type="text"] {
  background-color: #1d252e;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  font-weight: 500;
  height: 40px;
  outline: none;
  padding: 8px 8px 8px 20px; /* add left padding */
  width: 95%;
  font: inherit;
  outline: rgb(100, 100, 100) 1px solid;
  color: whitesmoke;
  transition: all 0.1s;
}

input[type="text"]:hover {
    outline: rgb(168, 168, 168) 1px solid;
}

input[type="text"]::placeholder {
  color: #b3b3b3a1;
  font-weight: 400;
}


.create_newstory {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    margin: 20px 0 0 0;
    display: flex;
    align-items: center;
    justify-content: left;
    border: 0px rgb(232, 255, 199) solid;
    border-radius: 10px;
    background-color: rgb(119 119 119 / 19%);
}

.postimage {
    height: 55px;
    border-radius: 100%;
    margin: 10px 10px;
    transition: all 0.1s;
}

.postimage:hover {
    cursor: pointer;
    filter: brightness(85%);
}

.selector {
    height: 100px;
}

.block {
  margin: 20px 0 0 0;
  width: 100%;
  height: 50px;
  display: flex;
}

.rectangle {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.1s;
}

.rectangle p {
  font-size: 24px;
  color: white;
  transition: all 0.1s;
}

</style>