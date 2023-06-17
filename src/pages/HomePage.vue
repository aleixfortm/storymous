<template>
    <feed-container v-if="isLoggedIn">
        <div class="create_newstory">
            <img class="postimage" src="../assets/img/default_blue.png" alt="profilepic">
            <router-link to="/storymous-migration/newpost" class="story_form">
                <input type="text" placeholder="Write new story" @click="navigateToNewPost">
            </router-link>
        </div>
    </feed-container>
    <feed-container v-else class="homepage-top">
        <div class="welcome-message">
            <div class="messagecontainer">
                <div class="innermessagecontainer">
                    Welcome to Storymous! <br>
                    Amazing stories await{{ modifiedText }}
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

    <component :is="selectedTab" :posts="posts"></component>

</template>


<script>
import { mapGetters } from 'vuex';
import { useRouter } from 'vue-router';
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
        return { $router: router };
    },
    data() {
        return {
            posts: {},
            selectedTab: 'latest-feed',
            openDialog: true,
            userLogged: true,
            text: " ",
            showCharacter: true
        }
    },
    mounted() {
    axios
        .get('https://api.npoint.io/786a14060decfb7e66d9')
        .then(response => {
            console.log(response)
            this.posts = response.data;
        })
        .catch(error => {
            console.log(error);
        }),

        setInterval(() => {
            this.showCharacter = !this.showCharacter; // Toggle showCharacter value every second
        }, 750);
        
    },
    methods: {
        setSelectedTab(tab) {
            console.log(this.currentUser)
            this.selectedTab = tab;
        },
        navigateToNewPost() {
            this.$router.push('/newpost');
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser']),

        modifiedText() {
            if (this.showCharacter) {
                return ""; // Replace character with underscore when showCharacter is false
            } else {
                return ""
            }

        }
    }

}
</script>


<style scoped>
.homepage-top {
    background-color: rgba(90, 90, 90, 0.301);
    padding: 20px 10px;
    border-radius: 10px;
}

.homepage-top:hover {
    background-color: rgba(90, 90, 90, 0.13);
}

.messagecontainer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: left;
}

.innermessagecontainer {
    width: auto; /*360px*/
    margin: 0 20px 100px 0;
    background-color: white;
    padding: 10px 20px 10px 20px;
    border-radius: 20px 20px 0 20px;
    font-size: x-large;
    font-weight: bold;
    cursor: default;
    animation: floatAnimation 4s ease-in infinite;
}

.welcome-message {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    margin: 0 10px 0 0;
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
    margin: 0 10px 100px 10px;
    width: auto; /*360px*/
    background-color: white;
    padding: 10px 20px 10px 20px;
    border-radius: 20px 20px 0 20px;
    font-size: large;
    font-weight: bold;
    cursor: default;

}

.welcome-message {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
}
}



@media (max-width: 480px) {
  .responsive-text {
    font-size: 14px; /* Further adjusted font size for even smaller screens */
  }

  .innermessagecontainer {
    margin: 0 10px 100px 10px;
    width: auto; /*360px*/
    background-color: white;
    padding: 10px 20px 10px 20px;
    border-radius: 20px 20px 0 20px;
    font-size: medium;
    font-weight: bold;
    cursor: default;
}

.welcome-message {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
}
}
/*
@keyframes floatAnimation {
  0% {
    transform: translateY(-10);
  }
  50% {
    transform: translateY(10);
  }
  100% {
    transform: translateY(-10);
  }
}
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
    border: 2px whitesmoke solid;
}

.postimage:hover {
    cursor: pointer;
    border: 2px rgb(201, 201, 201) solid;
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

}

.rectangle p {
  font-size: 24px;
  color: white;
}

</style>