<template>
    <div class="body">
        <div class="lower-body">
        <div class="section">
            <slot></slot>
        </div>
        <div class="section2" v-if="applicableRoute">
            <component :is="sidebarComponent"></component>
        </div>
        </div>
    </div>
</template>

<script>
import WelcomeSidebar from "@/components/sidebars/WelcomeSidebar.vue"
import HomeSidebar from "@/components/sidebars/HomeSidebar.vue"
import StorySidebar from "@/components/sidebars/StorySidebar.vue"

export default {
    components: {
        WelcomeSidebar,
        HomeSidebar,
        StorySidebar
    },
    data() {
        return {
            sidebarComponent: WelcomeSidebar, // Default component
            applicableRoutes: ["WelcomePage", "HomePage", "ChapterPage"]
        };
    },
    watch: {
        '$route.name': 'updateSidebarComponent',
    },
    methods: {
        updateSidebarComponent(routeName) {
            // Use routeName to determine which sidebar component to display
            if (routeName === 'WelcomePage') {
                this.sidebarComponent = WelcomeSidebar;
            } else if (routeName === 'HomePage') {
                this.sidebarComponent = HomeSidebar
            } else if (routeName === 'ChapterPage') {
                this.sidebarComponent = StorySidebar
            }
        },
    },
    computed: {
        applicableRoute() {
            const routeName = this.$route.name;
            return this.applicableRoutes.includes(routeName);
        }
    }
};
</script>

<style scoped>

.lower-body {
    padding: 3.5rem 0 0 0;
    display: flex;
    justify-content: center;
}

.section {
    height: fit-content;
    max-width: 700px;
    width: 100%;
}

.section2 {
    height: fit-content;
    max-width: 300px;
    width: 300px;
    height: 1000px;
    margin-left: 25px;
    margin-top: 10px;
}

@media (max-width: 1000px) {
    .section2 {
        display: none;
    }
}

</style>