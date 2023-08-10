<template>
    <astronaut-message 
        class="astro"
        :onomatopoeia="''" 
        :text="'In the depths of our galaxy lies a distant planet, where a mesmerizing forest thrives— a place where the ethereal story tree whispers secrets of cosmic wonders...'"
        :flipped="false">
    </astronaut-message>

    <div class="block">
        <div class="rectangle">
            <select-button 
            @click="setSelectedTab('latest-feed')" 
            :mode="selectedTab === 'following-feed' ? null : 'flat'"
            :selected="true">
                <div>Explore</div>
            </select-button>
        </div>
    </div>

    <latest-feed :posts="posts" :loading="loading"></latest-feed>
</template>

<script>
import { mapGetters } from 'vuex';
import { useRouter } from 'vue-router';
import { API_BASE_URL } from '../config';

import axios from 'axios';

import SelectButton from "../components/SelectButton.vue";
import LatestFeed from "../pages/subpages/LatestFeed.vue";
import AstronautMessage from '@/components/layout/messages/AstronautMessage.vue';

export default {
    components: {
        SelectButton,
        LatestFeed,
        AstronautMessage
    },
    setup() {
        const router = useRouter();
        return { router: router };
    },
    data() {
        return {
            posts: {},
            openDialog: true,
            userLogged: false,
            text: " ",
            showCharacter: true,
            loading: true,
        }
    },
    mounted() {
        if (this.isLoggedIn) {
            this.router.push("/home")
        } else {
            axios
            .get(`${API_BASE_URL}/posts`)
            .then(response => {
                this.posts = response.data;
                this.loading = false;
            })
            .catch(error => {
                console.log(error);
            });
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn']),
    },
}

</script>

<style scoped>
.astro {
    margin-top: -5px;
}

.nomargin {
    padding: 0px 0px;
    margin: 0px;
}

.testimage {
    width: 100%;
    border-radius: 10px;
    opacity: 1;
    margin: 20px 0 0 0;
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
    padding: 0px;
    border-radius: 10px;
    margin: 10px auto;
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
    display: flex;
    margin: 10px 0 0 0;
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