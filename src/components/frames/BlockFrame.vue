<template>
    <div class="body">
        <div class="lower-body">
        <div class="section">
            <slot></slot>
        </div>
        <div class="section2">
            <component :is="sidebarComponent"></component>
        </div>
        </div>
    </div>
</template>

<script>
import WelcomeSidebar from "@/components/sidebars/WelcomeSidebar.vue"
import HomeSidebar from "@/components/sidebars/HomeSidebar.vue"

export default {
    components: {
        WelcomeSidebar,
        HomeSidebar
    },
    data() {
        return {
            sidebarComponent: WelcomeSidebar, // Default component
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
            } else {
                this.sidebarComponent = WelcomeSidebar;
            }
        },
    },
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