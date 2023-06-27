import { createRouter, createWebHistory } from "vue-router";

import HomePage from "./pages/HomePage.vue";
import PostPage from "./pages/PostPage.vue";
import UserPage from "./pages/UserPage.vue";
import NewPost from "./pages/NewPost.vue";
import NotfoundPage from "./pages/NotfoundPage.vue";
import SettingsPage from "./pages/SettingsPage.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", component: HomePage },
        { path: "/home", redirect: "/" },
        { path: "/newpost", component: NewPost },
        { path: "/user/:id", component: UserPage },
        { path: "/post/:id", component: PostPage },
        { path: "/settings", component: SettingsPage },
        { path: "/:catchAll(.*)", component: NotfoundPage } // named redirect route for any undefined route
    ],
});

export default router;