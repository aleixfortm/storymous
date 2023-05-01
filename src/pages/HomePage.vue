<template>

        <div class="selector">
            <ul>
                <li>New</li>
                <li>Following</li>
            </ul>
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

export default {
    components: {
        //FeedContainer,
        PostContainer
    },
    data() {
        return {
            posts: [
                { id: '1', title: 'Pollancret petit', content: 'Lorem ipsum fsdfsadf dsfdsafdsf dsfdsaf dsfdasf dsfsadfdsafdsf dsfdsa fdsaf dsf sda' },
                { id: '2', title: 'Ato mar porc ulo', content: 'sdfsdfsdfdsfds fdsf dsafd sfdsf dsfsd fds fsdf sdfds fdsa afsdf dsf sdaf dfadsfdsafdsfds fdsf asdfdas f' },
            ],
        }
    }
}


</script>


<style scoped>

.selector {
    height: 100px;
}

ul {
    padding: 10px 100px;
}

li {
    list-style: none;
    width: 50%;
    justify-content: center;
    align-items: center;
    text-align: center;
}


</style>