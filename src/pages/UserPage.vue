<template>
    <feed-container :key="currentParameter">
        <section v-if="ownProfile()" class="section_title">
            My profile
        </section>
        <section v-else class="section_title">
            {{ profileUsername }}'s profile
        </section>
        <section class="profile-box">
            <div class="imageblock">
                <img class="postimage" src="../assets/img/default_blue.png" alt="profilepic">
            </div>
            <div class="statsblock">
                <div class="topblock">
                    <div class="name-color">
                        <div class="color-scheme"></div>
                        <div class="username">@{{ profileUsername }}</div>
                    </div>
                    <button v-if="!ownProfile()" class="followbutton">Follow</button>
                </div>
                <div class="stats">
                    <div class="count-block">
                        <b>Stories</b>
                        <div class="count-block__num">3</div>
                    </div>
                    <div class="count-block">
                        <b>Followers</b>
                        <div class="count-block__num">10</div>
                    </div>
                    <div class="count-block">
                        <b>Following</b>
                        <div class="count-block__num">24</div>
                    </div>
                </div>
                <div class="stats-bio">
                    <b>Bio</b>
                    <div class="bio-content">yo! My name's <b>{{ profileUsername }}</b> and I love Storymous! Follow me to be up to date with my content :) </div>
                </div>
                <div v-if="ownProfile()" class="miscbuttons">
                    <button class="settingsbutton" @click="goToSettings">Edit profile</button>
                    <button class="logoutbutton" @click="logout()">Log out</button>
                </div>
            </div>
        </section>

        <section v-if="ownProfile()" class="section_title">
            My posts
        </section>
        <section v-else class="section_title">
            {{ profileUsername }}'s posts
        </section>
        <div v-if="loading" class="loader-container">
            <div class="lds-facebook">
                <div></div>
                <div></div>
                <div></div>
            </div>
                <span class="loader-text">Harvesting user stories...</span>
            </div>
        <div v-else>
            <post-container 
                v-for="post in posts"
                :key="post._id"
                :_id="post._id"
                :title="post.title"
                :content="post.content"
                :username="post.username"
                :postComment="post.post_comment"
                :date="post.date"
                :picture="post.picture"
                :color="post.color">
            </post-container>
        </div>
    </feed-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import axios from 'axios';
import { useRouter } from 'vue-router';

import FeedContainer from "../components/layout/FeedContainer.vue";
import PostContainer from "../components/layout/PostContainer.vue";

export default {
    setup() {
        const router = useRouter();
        return { router: router };
    },
    data() {
        return {
            posts: [],
            profileUsername: null,
            loading: true
        }
    },
    components: {
        FeedContainer,
        PostContainer
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser']),
        currentParameter() {
            return this.$route.params.id; // Replace "parameter" with the actual name of your URL parameter
        },
    },
    mounted() {
        this.profileUsername = this.$route.params.id;
        console.log(this.$route.params.id)
    axios
        .get(`http://127.0.0.1:5000/posts/${this.profileUsername}`)
        .then(response => {
            this.posts = response.data;
            this.loading = false;
        })
        .catch(error => {
            console.log(error);
        });
    },
    watch: {
        currentParameter() {
            this.profileUsername = this.$route.params.id;
        },
    },
    methods: {
        ...mapActions('auth', ['logout']),
        ownProfile() {
            if (this.profileUsername === this.currentUser) {
                return true;
            } else {
                return false;
            }
        },
        goToSettings() {
            this.router.push('/storymous/settings');
        }
    }
}

</script>

<style scoped>
.loader-text {
    background-color: whitesmoke;
    color: rgb(0, 0, 0);
    padding: 5px 10px;
    border-radius: 15px;
    font-weight: bold;
}

.loader-container {
    margin: 40px 0 0 0;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.lds-facebook {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-facebook div {
  display: inline-block;
  position: absolute;
  left: 8px;
  width: 16px;
  background: #fff;
  animation: lds-facebook 1.2s cubic-bezier(0, 0.5, 0.5, 1) infinite;
}
.lds-facebook div:nth-child(1) {
  left: 8px;
  animation-delay: -0.24s;
}
.lds-facebook div:nth-child(2) {
  left: 32px;
  animation-delay: -0.12s;
}
.lds-facebook div:nth-child(3) {
  left: 56px;
  animation-delay: 0;
}
@keyframes lds-facebook {
  0% {
    top: 8px;
    height: 64px;
  }
  50%, 100% {
    top: 24px;
    height: 32px;
  }
}

.name-color {
    display: flex;
}

.color-scheme {
    border-radius: 500%;
    background-color: red;
    width: 25px;
    height: 25px;
    align-self: center;
    margin: 0 15px 0 0;
    box-shadow: 0px 0px 10px 2px rgba(255, 0, 0, 0.479);
}

.followbutton {
    height: 30px;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(0, 255, 98);
    cursor: pointer;
    font-size: 15px;
    width: 80px;
    margin: 10px 10px 10px 0;
    background-color: #59ff9138;
    border-radius: 4px;
    transition: all 0.1s;
}

.followbutton:hover {
    background-color: #41bb6a2f;
}

.miscbuttons {
    display: flex;
    flex-direction: row;
    margin: 10px 0 0px 0;
    height: 30px;
    align-items: center;
    justify-content: flex-end;
    width: 80%;
    align-self: end;
}

.logoutbutton {
    height: 30px;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 15px;
    width: 85px;
    margin: 10px 10px 10px 20px;
    background-color: #ff0000cc;
    border-radius: 4px;
    align-items: center;
    transition: all 0.1s;
}

.logoutbutton:hover {
    background-color: #ff00006c;
}

.settingsbutton {
    height: 30px;
    font-family: inherit;
    border: none;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 15px;
    width: 125px;
    margin: 10px 10px 10px 0;
    background-color: rgba(0, 0, 0, 0.459);
    border-radius: 4px;
    align-items: center;
    transition: all 0.1s;
}

.settingsbutton:hover {
    background-color: rgba(0, 0, 0, 0.185);
}

.section_title {
  padding-bottom: 2px;
  margin: 35px 10px 20px 10px;
  font-size: larger;
  font-weight: bold;
  color: rgb(0, 248, 174);
  border-bottom: 2px solid rgb(180, 255, 233);
}

.profile-box {
    display: flex;
    flex-direction: row;
    background-color: rgb(119 119 119 / 19%);
    padding: 10px;
    border-radius: 10px;
}

.topblock {
    display: flex;
    flex-direction: row;
    width: 100%;
    justify-content: space-evenly;
    align-items: center;
    margin: 25px 0 0 0;
}

.imageblock {
    display: flex;
    justify-content: center;
    align-items: center;
    height: auto;
    width: 340px;
}

.statsblock {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: fit-content;
    width: 340px;
    
}

.username {
    color: whitesmoke;
    font-weight: bold;
    font-size: x-large;
}

.stats {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin: 20px 0 0 0;
    width: 100%;
    color: whitesmoke;
    transition: all 0.1s;
}

.count-block {
    display: flex;
    flex-direction: column;
    background-color: rgba(151, 151, 151, 0.192);
    padding: 5px;
    border-radius: 8px;
    cursor: pointer;
}

.count-block:hover {
    background-color: rgba(192, 192, 192, 0.192);
}

/*
.stats-bio {
    background-color: rgba(151, 151, 151, 0.192);
    border-radius: 8px;
    padding: 5px;
    margin: 30px 10px 5px 10px;
    color: whitesmoke;
}
*/
.stats-bio {
    background-color: rgb(255, 255, 255);
    border-radius: 10px 10px 10px 10px;
    padding: 10px;
    margin: 30px 10px 5px 10px;
    color: rgb(0, 0, 0);
}

.postimage {
    height: 275px;
    border-radius: 500%;
    border: 6px solid whitesmoke;
}

@media screen and (max-width: 650px) {
    .profile-box {
        flex-direction: column;
        width: fit-content;
        margin: auto;
    }

    .topblock {
        margin: 0px 0 0 0;
    }

    .statsblock {
        height: fit-content;
        margin: 15px 0 0 0;
    }
}

</style>