<template>
    <feed-container>
        <template v-if="showData">
            <contributors-box :contributors="getContributors"></contributors-box>
        </template>       
        <template v-else>
            <empty-box v-for="i in 1" :key="i"></empty-box>
        </template>
    </feed-container>
</template>

<script>
import FeedContainer from '../frames/FeedContainer.vue';
import ContributorsBox from './welcome/ContributorsBox.vue';
import EmptyBox from "./boxes/EmptyBox.vue"

import { mapGetters } from 'vuex';
import { mapActions } from "vuex";

export default {
    name: "StorySidebar",
    components: {
        FeedContainer,
        ContributorsBox,
        EmptyBox
    },
    data() {
        return {
            status: true,
            showData: false
        }
    },
    computed: {
        ...mapGetters('chapterData', ['getContributors', 'getNewStatus']),
    },
    methods: {
        ...mapActions('chapterData', ['setNewStatus']),
        toggleNewStatus() {
        this.setNewStatus(!this.newStatus);
        }
    },
    watch: {
        getNewStatus(newVal) {
            if (newVal) {
                this.showData = true
                setTimeout(() => {
                this.setNewStatus(false);
                }, 1000);
            }
        }
    },

}
</script>

<style scoped>
div {
    color: white;
}
</style>