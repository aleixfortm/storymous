<template>
    <div class="block">
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

    <component :is="selectedTab" :posts="posts"></component>

</template>


<script>
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
                /*
                { 
                    id: '1', 
                    title: 'Pollancret petit', 
                    content: 'Lorem ipsum fsdfsadf dsfdsafdsf dsfdsaf dsfdasf dsfsadfdsafdsf dsfdsa fdsaf dsf sda',
                    username: "pollancre",
                    postComment: "Long live CSGO boys!!!",
                    date: "2 days ago",
                },
                { 
                    id: '2', 
                    title: 'Pollancret petit', 
                    content: 'Lorem ipsum fsdfsadf dsfdsafdsf dsfdsaf dsfdasf dsfsadfdsafdsf dsfdsa fdsaf dsf sda',
                    username: "pollancre",
                    postComment: "Long live CSGO boys!!!",
                    date: "2 days ago",
                },
                { 
                    id: '3', 
                    title: 'Pollancret petit', 
                    content: 'Lorem ipsum fsdfsadf dsfdsafdsf dsfdsaf dsfdasf dsfsadfdsafdsf dsfdsa fdsaf dsf sda',
                    username: "pollancre",
                    postComment: "Long live CSGO boys!!!",
                    date: "2 days ago",
                },
                */
            selectedTab: 'latest-feed',
            openDialog: true
        }
    },
    mounted() {
    axios
        .get('https://api.npoint.io/786a14060decfb7e66d9')
        .then(response => {
            this.posts = response.data;
            console.log(this.posts)
        })
        .catch(error => {
            console.log(error);
        });
    },
    methods: {
        setSelectedTab(tab) {
            this.selectedTab = tab;
        }
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
  width: 50%;
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