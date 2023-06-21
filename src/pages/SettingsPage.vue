<template>
    <feed-container>
        <section class="section_title">
            User settings
        </section>
        <div class="setting">
            <button class="access-button">Profile picture</button>
            <span class="description">Choose a new profile picture</span>
        </div>
        <div class="setting">
            <button class="access-button orange">Profile color</button>
            <span class="description">Choose a color scheme for your profile, which will also be applied to your posts</span>
        </div>
        <div class="setting">
            <button class="access-button purple">Profile bio</button>
            <span class="description">Change your profile's bio</span>
        </div>
        <section class="section_title"></section>
        <component :is="selectedSetting"></component>
    </feed-container>
</template>

<script>
import { useRouter } from 'vue-router';
import { mapGetters } from 'vuex';

import FeedContainer from '@/components/layout/FeedContainer.vue';



export default {
    setup() {
        const router = useRouter();
        return { router: router };
    },
    components: {
        FeedContainer
    },
    mounted() {
        if (this.isLoggedIn === false) {
            this.router.push('/storymous/home');
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser']),
    }
}

</script>

<style scoped>
.setting {
    margin: 40px 10px;
    display: flex;
    align-items: center;
    justify-content: left;
}

.section_title {
  padding-bottom: 2px;
  margin: 35px 10px 10px 10px;
  font-size: larger;
  font-weight: bold;
  color: rgb(0, 248, 174);
  border-bottom: 2px solid rgb(180, 255, 233);
}

.description {
    color: whitesmoke;
}

.access-button {
    height: fit-content;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(0, 0, 0);
    cursor: pointer;
    font-size: 15px;
    width: fit-content;
    margin: 0px 10px 0px 0;
    background-color: rgb(0, 153, 255);
    border-radius: 4px;
    font-weight: bold;
}

.orange {
    background-color: rgb(255, 145, 0);
}

.purple {
    background-color: rgb(183, 0, 255);
}

.access-button:hover {
    background-color: rgba(0, 153, 255, 0.541);
}

</style>