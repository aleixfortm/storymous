import { createRouter, createWebHistory } from "vue-router";

import HomePage from "@/pages/homepage/HomePage.vue"
import UserPage from "@/pages/userpage/UserPage.vue";
import NewPost from "@/pages/homepage/NewPost.vue";
import NotfoundPage from "@/pages/homepage/NotfoundPage.vue";
import SettingsPage from "@/pages/userpage/SettingsPage.vue";
import ChapterPage from "@/pages/postpage/ChapterPage.vue";
import WelcomePage from "@/pages/homepage/WelcomePage.vue"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", component: WelcomePage },
        { path: "/home", component: HomePage },
        { path: "/newpost", component: NewPost },
        { path: "/user/:id", component: UserPage },
        { path: "/chapter/:id", component: ChapterPage },
        { path: "/settings", component: SettingsPage },
        { path: "/:catchAll(.*)", component: NotfoundPage } // named redirect route for any undefined route
    ],
});

export default router;