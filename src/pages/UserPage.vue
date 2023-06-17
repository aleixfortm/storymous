<template>
    <feed-container>
        <section class="section_title">
            My profile
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
  margin: 35px 0 20px 10px;
  font-size: larger;
  font-weight: bold;
  color: rgb(0, 248, 174);
  border-bottom: 2px solid rgb(180, 255, 233);
}

</style>