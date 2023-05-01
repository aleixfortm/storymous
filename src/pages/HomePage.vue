<template>

    <div class="block">
        <div class="rectangle">
            <select-button @click="setSelectedTab('latest')" :mode="selectedTab === 'following' ? null : 'flat'">
                <div>Latest</div>
            </select-button>
        </div>

        <div class="rectangle">
            <select-button @click="setSelectedTab('following')" :mode="selectedTab === 'following' ? 'flat' : null">
                <div>Following</div>
            </select-button>
        </div>
    </div>

    <post-container
        v-for="post in posts"
        :key="post.id"
        :title="post.title"
        :content="post.content">
    </post-container>

</template>


<script>
//import FeedContainer from "../components/layout/FeedContainer.vue";
import PostContainer from "../components/layout/PostContainer.vue";
import SelectButton from "../components/SelectButton.vue";

export default {
    components: {
        //FeedContainer,
        PostContainer,
        SelectButton
    },
    data() {
        return {
            posts: [
                { id: '1', title: 'Pollancret petit', content: 'Lorem ipsum fsdfsadf dsfdsafdsf dsfdsaf dsfdasf dsfsadfdsafdsf dsfdsa fdsaf dsf sda' },
                { id: '2', title: 'Ato mar porc ulo', content: 'sdfsdfsdfdsfds fdsf dsafd sfdsf dsfsd fds fsdf sdfds fdsa afsdf dsf sdaf dfadsfdsafdsfds fdsf asdfdas f' },
            ],
            selectedTab: 'latest',
        }
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