<template>
    <feed-container v-if="isLoggedIn">
        <div class="create_newstory">
            <img class="postimage" src="../assets/img/default_blue.png" alt="profilepic">
            <router-link to="/newpost" class="story_form">
                <input type="text" placeholder="Write new story" @click="navigateToNewPost">
            </router-link>
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
    setup() {
        const router = useRouter();
        return { $router: router };
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
        },
        navigateToNewPost() {
            this.$router.push('/newpost');
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser']),
    }

}
</script>


<style scoped>
.story_form {
    width: 100%;
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