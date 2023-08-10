<template>
    
    <feed-container :key="currentParameter">
        <login-message v-if="!isLoggedIn" :text="'to follow other users'"></login-message>
        <section v-if="ownProfile()" class="section_title">
            My profile
        </section>
        <section v-else class="section_title">
            {{ profileUsername }}'s profile
        </section>
        <section :class="profileBoxClass" v-if="userPicture">
            <profile-picture
                v-if="userPicture"
                :picture="userPicture">
            </profile-picture>
            <profile-picture
                v-else
                :picture="'moon_default_avatar-min.png'"
            ></profile-picture>
            <div class="statsblock">
                <div class="topblock">
                    <div class="name-color">
                        <div class="username">@{{ profileUsername }}</div>
                    </div>
                    <button 
                        v-if="!ownProfile() && isLoggedIn" 
                        class="followbutton"
                        :class="{ following: isFollowing, disabled: isFollowButtonDisabled }" 
                        @click="followAction"
                        :disabled="isFollowButtonDisabled">
                        <div v-if="!isFollowing" class="d-flex align-items-center justify-content-center"><span class="material-symbols-outlined">person_add</span></div>
                        <div v-else class="d-flex align-items-center justify-content-center"><span class="material-symbols-outlined">remove</span></div>
                    </button>
                </div>
                <div class="stats-container">
                    <div class="stats user-select-none">
                        <div class="count-block" @mouseover="showLeavesTooltip = true" @mouseout="showLeavesTooltip = false">
                            <span class="material-symbols-outlined colored-icon">nest_eco_leaf</span>
                            <div class="separator-stat"></div>
                            <div class="count-block__num">{{ nLeaves }}</div>
                            <small-tooltip :condition="showLeavesTooltip" :text="'Leaves'" :top="'45px'"></small-tooltip>
                        </div>
                        
                        <div class="count-block" @mouseover="showStoriesTooltip = true" @mouseout="showStoriesTooltip = false">
                            <span class="material-symbols-outlined">import_contacts</span>
                            <div class="separator-stat"></div>
                            <div class="count-block__num">{{ nStories }}</div>
                            <small-tooltip :condition="showStoriesTooltip" :text="'Stories'" :top="'45px'"></small-tooltip>
                        </div>
                        <div class="count-block" @mouseover="showFollowersTooltip = true" @mouseout="showFollowersTooltip = false">
                            <span class="material-symbols-outlined">group</span>
                            <div class="separator-stat"></div>
                            <div class="count-block__num">{{ userFollowers.length }}</div>
                            <small-tooltip :condition="showFollowersTooltip" :text="'Followers'" :top="'45px'"></small-tooltip>
                        </div>
                        <div class="count-block" @mouseover="showFollowingTooltip = true" @mouseout="showFollowingTooltip = false">
                            <span class="material-symbols-outlined">group_add</span>
                            <div class="separator-stat"></div>
                            <div class="count-block__num">{{ userFollowing.length }}</div>
                            <small-tooltip :condition="showFollowingTooltip" :text="'Following'" :top="'45px'"></small-tooltip>
                        </div>
                    </div>
                </div>
                <div class="stats-bio">
                    <div class="bio-title">Bio<div class="separator-stat"></div><span class="material-symbols-outlined">history_edu</span></div>
                    <div class="bio-content">{{ userBio }}</div>
                </div>
                <div v-if="ownProfile() && isLoggedIn" class="miscbuttons">
                    <settings-button :text="'SETTINGS'" @click="goToSettings">
                        <span class="material-symbols-outlined margin1">settings</span>
                    </settings-button>
                    <logout-button :text="'LOG OUT'" @click="logout()">
                        <span class="material-symbols-outlined margin1">logout</span>
                    </logout-button>
                </div>
            </div>
        </section>
        <section class="profile-box centered" v-else>
            <div v-if="loading" class="loader-container">
                <div class="spinner-border text-light mb-3" style="width: 5rem; height: 5rem;" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            <span class="loader-text">Spotting authors nearby...</span>
        </div>
        </section>

        <section v-if="ownProfile()" class="section_title">
            My posts
        </section>
        <section v-else class="section_title">
            {{ profileUsername }}'s posts
        </section>
        <div v-if="loading" class="loader-container">
            <div class="spinner-border text-light mb-3" style="width: 5rem; height: 5rem;" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <span class="loader-text">Fetching user stories...</span>
        </div>
        <div v-else-if="posts.length > 0">
            <div v-for="post in posts" :key="post._id.$oid">
                <template v-if="post.type === 'prologue'">
                    <post-container
                        :_id="post._id"
                        :title="post.title"
                        :content="post.content"
                        :username="post.username"
                        :postComment="post.comment"
                        :date="post.date"
                        :picture="post.picture"
                        :color="post.color"
                        :views="post.views"
                        :comments="post.user_comments"
                        :tags="post.tags"
                        :leaves="post.leaves"
                        :feedMode="true">
                    </post-container>
                </template>
                <template v-else>
                    <continuestoryfeed-container
                        :_id="post._id"
                        :storyId="post.story_id"
                        :parentChapterId="post.parent_chapter_id"
                        :content="post.content"
                        :chapterName="post.chapter_name"
                        :chapterNum="post.chapter_num"
                        :username="post.username"
                        :color="post.color"
                        :storyTitle="post.story_title"
                        :postComment="post.comment"
                        :date="post.date"
                        :picture="post.picture"
                        :leaves="post.leaves"
                        :views="post.views"
                        :tags="post.tags">
                    </continuestoryfeed-container>
                </template>
                </div>
            </div>
            <div v-else>
            <astronaut-message :onomatopoeia="'crick crick'"
            :text="'Countless tales have been told since the beginning of time, yet none have borne their signature. What might they be doing?'"></astronaut-message>
        </div>
    </feed-container>

</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import { useRouter } from 'vue-router';
import { API_BASE_URL } from '../config';
import axios from 'axios';

import FeedContainer from "../components/layout/FeedContainer.vue";
import PostContainer from "@/components/layout/feedposts/PostContainer.vue";
import ProfilePicture from '@/components/layout/ProfilePicture.vue';
import ContinuestoryfeedContainer from '@/components/layout/feedposts/ContinuestoryfeedContainer.vue';
import AstronautMessage from '@/components/layout/messages/AstronautMessage.vue';
import SettingsButton from '@/components/layout/SettingsButton.vue';
import LogoutButton from '@/components/layout/LogoutButton.vue';
import SmallTooltip from '@/components/layout/SmallTooltip.vue';
import LoginMessage from '@/components/layout/messages/LoginMessage.vue';

export default {
    components: {
        FeedContainer,
        PostContainer,
        ProfilePicture,
        ContinuestoryfeedContainer,
        AstronautMessage,
        SettingsButton,
        LogoutButton,
        SmallTooltip,
        LoginMessage
    },
    setup() {
        const router = useRouter();
        return { router: router };
    },
    data() {
        return {
            posts: [],
            bio: null,
            profileUsername: null,
            loading: true,
            userPicture: "",
            userColor: "",
            userBio: "",
            nStories: 0,
            nLeaves: 0,
            userFollowers: 0,
            userFollowing: 0,
            isFollowing: null,
            isFollowButtonDisabled: false,
            showLeavesTooltip: false,
            showStoriesTooltip: false,
            showFollowersTooltip: false,
            showFollowingTooltip: false
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched", "userFetchedBio", "nFetchedPosts", "nFetchedFollowers", "nFetchedFollowing", "nFetchedLeaves"]),
        currentParameter() {
            return this.$route.params.id; // Replace "parameter" with the actual name of your URL parameter
        },
        imgSource() {
            return require('../assets/img/' + this.userColor);
        },
        profileBoxClass() {
            return `profile-box ${this.userColor}`;
        },
    },
    mounted() {
        this.fetchDataComponent();
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
        followAction() {

            this.isFollowButtonDisabled = true;

            const data_packet = {
                action: !this.isFollowing ? "follow" : "unfollow",
                user_being_followed: this.profileUsername,
                user_follows: this.currentUser
            }

            axios
                .post(`${API_BASE_URL}/follow`, data_packet)
                .then(response => {
                    const data = response.data;
                    if (data == "Success") {
                        this.isFollowing = !this.isFollowing
                    }
                    this.isFollowButtonDisabled = false;
                    if (this.isFollowing) {
                        this.userFollowers.push(this.currentUser)
                    } else {
                        const index = this.userFollowers.indexOf(this.currentUser);
                        if (index !== -1) {
                            this.userFollowers.splice(index, 1);
                        }
                    }
                    
                })

                .catch(error => {
                    console.log(error);
                    this.isFollowButtonDisabled = false;
                });
        },
        goToSettings() {
            this.$router.push('/settings');
        },
        fetchDataComponent() {
            this.profileUsername = this.$route.params.id;
            if (this.ownProfile()) {
                this.userPicture = this.userFetchedPicture;
                this.userColor = this.colorFetched;
                this.userBio = this.userFetchedBio;
                this.nStories = this.nFetchedPosts;
                this.userFollowers = this.nFetchedFollowers;
                this.userFollowing = this.nFetchedFollowing;
                this.nLeaves = this.nFetchedLeaves;

            axios
                .get(`${API_BASE_URL}/posts/${this.profileUsername}`)
                .then(response => {
                    const data = response.data;
                    console.log(data)
                    this.posts = data;
                    this.loading = false;
                })
                .catch(error => {
                    console.log(error);
                });
            } else {
            axios
                .get(`${API_BASE_URL}/user/${this.profileUsername}`)
                .then(response => {
                    const data = response.data;
                    this.posts = data.posts;
                    const userData = data.user_data;
                    this.userPicture = userData.picture;
                    this.userColor = userData.color;
                    this.userBio = userData.bio; 
                    this.nStories = userData.started_stories + userData.continued_stories;
                    this.userFollowers = userData.followers;
                    this.userFollowing = userData.following;
                    this.nLeaves = userData.leaves;
                    this.loading = false;

                    if (this.isLoggedIn) {
                        if (userData.followers.includes(this.currentUser)) {
                            this.isFollowing = true;
                        } else {
                            this.isFollowing = false;
                        }
                    }
                })
                .catch(error => {
                    console.log(error);
                });
            }
        }
    }
}

</script>

<style scoped>

.colored-icon {
    color: rgb(0, 255, 106);
    font-variation-settings:
    'FILL' 1,
    'wght' 600,
    'GRAD' 0,
    'opsz' 200
}

.separator-stat {
    margin: 0 2px;
}

.bio-content {
    color: rgba(255, 255, 255, 0.836);
}

.disabled {
  opacity: 0.5; 
  pointer-events: none; 
  cursor: default;
}

.followbutton.following {
  background-color: #ff7b009c;
  color: #fffb00f6;
  text-align: center;
  width: auto;
}

.followbutton.following:hover {
  background-color: #ff7b006e;
  color: #fffb00f6;
}

.separator {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.stats-container {
    width: 100%;
    padding: 0 35px;

}

.centered {
    justify-content: center;
    align-items: center;
    height: 300px
}

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

.name-color {
    display: flex;
}

.color-scheme {
    border-radius: 500%;
    background-color: rgb(0, 183, 255);
    width: 25px;
    height: 25px;
    align-self: center;
    margin: 0 15px 0 0;
    box-shadow: 0px 0px 10px 2px rgba(0, 183, 255, 0.575);
}

.followbutton {
    height: 30px;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(0, 255, 98);
    cursor: pointer;
    font-size: 15px;
    margin: 0 0 0 8px;
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
    margin: 10px 0 5px 0;
    height: 30px;
    align-items: center;
    justify-content: flex-end;
    width: 240px;
    align-self: end;
    justify-content: space-around;
}

.logoutbutton {
    display: flex;
    height: fit-content;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 15px;
    margin: 10px 10px 10px 20px;
    background-color: #ff0000af;
    border-radius: 4px;
    align-items: center;
    transition: all 0.1s;
}

.logoutbutton:hover {
    background-color: #ff00006c;
}

.settingsbutton {
    display: flex;
    font-family: inherit;
    border: none;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 15px;
    width: fit-content;
    margin: 10px 0px 10px 0;
    background-color: rgba(0, 0, 0, 0.342);
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
    border-radius: 5px;
}

.profile-box.salmon {
    border: 4px rgb(255, 109, 93) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 109, 93);
}

.profile-box.red {
    border: 4px rgb(255, 25, 0) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 25, 0);
}

.profile-box.blue {
    border: 4px rgb(0, 153, 255) solid;
    box-shadow: 0px 0px 5px 2px rgb(0, 153, 255);
}

.profile-box.green {
    border: 4px rgb(55, 182, 97) solid;
    box-shadow: 0px 0px 5px 2px rgb(55, 182, 97);
}

.profile-box.yellow {
    border: 4px rgb(255, 217, 0) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 217, 0);
}

.profile-box.white {
    border: 4px rgb(255, 255, 255) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 255, 255);
}

.profile-box.purple {
    border: 4px rgb(183, 0, 255) solid;
    box-shadow: 0px 0px 5px 2px rgb(183, 0, 255);
}

.profile-box.pink {
    border: 4px rgb(255, 0, 179) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 0, 179);
}

.profile-box.orange {
    border: 4px rgb(255, 145, 0) solid;
    box-shadow: 0px 0px 5px 2px rgb(255, 145, 0);
}

.topblock {
    display: flex;
    flex-direction: row;
    width: 100%;
    justify-content: center;
    align-items: center;
    margin: 0px 0 0 0;
}


.statsblock {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: fit-content;
    margin: 10px 0;
    width: 340px;
    height: auto;
}

.username {
    color: whitesmoke;
    font-weight: bold;
    font-size: x-large;
}

.stats {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 5px 0px 0 0px;
    border-radius: 2px;
    padding: 5px;
    width: 100%;
    color: whitesmoke;

    transition: all 0.1s;
}

.count-block {
    position: relative;
    display: flex;
    padding: 5px;
    border-radius: 8px;
    align-items: center;
    cursor: pointer;
}

.count-block:hover {
    background-color: rgba(121, 121, 121, 0.089);
}

.bio-title {
    color: rgb(245, 245, 245);
    display: flex;
    align-items: center;
    font-weight: bold;
}

.stats-bio {
    background-color: #f5f5f51a;
    border-radius: 5px;
    padding: 10px;
    margin: 20px 10px 15px 10px;
}

@media screen and (max-width: 700px) {
    .profile-box {
        flex-direction: column;
        width: 100%;
        margin: auto;
        align-items: center;
        
    }

    .topblock {
        margin: 0px 0 0 0;
    }

    .statsblock {
        height: fit-content;
        margin: 15px 0 0 0;
    }
}

@media screen and (max-width: 340px) {
    .statsblock {
        width: 100%;
    }
}

</style>