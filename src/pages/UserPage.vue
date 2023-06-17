<template>
    <feed-container>
        <section class="section_title">
            My profile
        </section>
        <section class="profile-box">
            <div class="imageblock">
                <img class="postimage" src="../assets/img/default_blue.png" alt="profilepic">
            </div>
            <div class="statsblock">

            </div>
        </section>
    </feed-container>
</template>

<script>
import { mapGetters } from 'vuex';
//import { useRouter } from 'vue-router';

import FeedContainer from "../components/layout/FeedContainer.vue"

export default {
    components: {
        FeedContainer,
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser']),
    }
}

</script>

<style scoped>
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

.imageblock {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 340px;
    width: 340px;
}

.statsblock {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 340px;
    width: 340px;
}

.postimage {
    height: 275px;
    border-radius: 500%;
}

</style>