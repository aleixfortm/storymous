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
        { path: "/storymous/", component: HomePage },
        { path: "/storymous/home", redirect: "/storymous/" },
        { path: "/storymous/newpost", component: NewPost },
        { path: "/storymous/user/:id", component: UserPage },
        { path: "/storymous/post/:id", component: PostPage },
        { path: "/storymous/settings", component: SettingsPage },
        { path: "/storymous/:catchAll(.*)", component: NotfoundPage } // named redirect route for any undefined route
    ],
});

export default router;