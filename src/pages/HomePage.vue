<template>
    <feed-container v-if="isLoggedIn">
        <div class="create_newstory">
            <img class="postimage" src="../assets/img/default_blue.png" alt="profilepic">
            <form>
                <input type="text" placeholder="Write new story" @input="search">
            </form>
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
import axios from 'axios';

import SelectButton from "../components/SelectButton.vue";
import LatestFeed from "../pages/subpages/LatestFeed.vue";
import FollowingFeed from "../pages/subpages/FollowingFeed.vue";

export default {
    components: {
        //FeedContainer,
        SelectButton,
        LatestFeed,
        FollowingFeed
    },
    data() {
        return {
            posts: [],
            selectedTab: 'latest-feed',
            openDialog: true,
            userLogged: true
        }
    },
    mounted() {
    axios
        .get('https://api.npoint.io/786a14060decfb7e66d9')
        .then(response => {
            console.log(response)
            this.posts = response.data;
            console.log(this.posts)
        })
        .catch(error => {
            console.log(error);
        });
    },
    methods: {
        setSelectedTab(tab) {
            console.log(this.currentUser)
            this.selectedTab = tab;
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser']),
    }

}
</script>


<style scoped>
form {
display: block;
width: 100%;
margin: 0 20px 0 0;
}

input[type="text"] {
  background-color: #333c46;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  font-weight: 500;
  height: 40px;
  outline: none;
  padding: 8px 8px 8px 20px; /* add left padding */
  width: 100%;
  font: inherit;
}

input[type="text"]:hover {
    outline: white;
}

input[type="text"]::placeholder {
  color: #b3b3b3a1;
  font-weight: 400;
}

input[type="text"]:focus {
  outline: none;
  color: #e2e2e2;
  background-color: #21272e;
  box-shadow: 0 0 0 2px #a1abbb;
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
    border: 2px rgb(216, 255, 161) solid;
    border-radius: 20px;
}

.create_newstory:hover {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    margin: 20px 0 0 0;
    display: flex;
    align-items: center;
    justify-content: left;
    border: 2px rgb(188, 255, 88) solid;
    border-radius: 20px;
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