<template>
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