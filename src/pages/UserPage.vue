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
                <div class="topblock">
                    <div class="username">@{{ currentUser }}</div>
                    <button>Follow</button>
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
    height: 340px;
    width: 340px;
}

.statsblock {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 340px;
    width: 340px;
}

.username {
    color: whitesmoke;
    font-weight: bold;
    font-size: larger;
}

.stats {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin: 20px 0 0 0;
    width: 100%;
    color: whitesmoke;
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

.postimage {
    height: 275px;
    border-radius: 500%;
}

</style>