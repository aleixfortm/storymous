<template>
    POLLANCRERA <br><br>LOLOLOLOLOLO
    <post-container
    :key="post._id"
    :_id="post._id"
    :title="post.title"
    :content="post.preview"
    :username="post.username"
    :postComment="post.post_comment"
    :date="post.date"
    :extendedLength="post.extended_length"
    :imgName="post.random_img">
    </post-container>
</template>

<script>
import PostContainer from '@/components/layout/PostContainer.vue'

import axios from 'axios';

export default {
    components: {
        PostContainer,

    },
    data() {
        return {
            post: {
                _id: "982989",
                title: "LOL",
                preview: "none",
                username: "nnana",
                post_comment: "sadfdsafsdafdfa",
                date: "2321321",
                extended_length: true,
                random_img: "home"
            }

        }
    },
    methods: {
        handleSelectedPost(post) {
            console.log("pollancre")
            console.log(post)
        }
    },
    mounted() {
    axios
        .get('https://api.npoint.io/786a14060decfb7e66d9')
        .then(response => {
            //console.log(response)
            this.posts = response.data;
        })
        .catch(error => {
            console.log(error);
        })
    }
}

</script>

