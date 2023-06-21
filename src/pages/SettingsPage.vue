<template>
    <feed-container>
        POLLANCRE
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