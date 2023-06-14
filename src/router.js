import { createRouter, createWebHistory } from "vue-router";

import HomePage from "./pages/HomePage.vue";
import PostPage from "./pages/PostPage.vue";
import UserPage from "./pages/UserPage.vue";
import NotfoundPage from "./pages/NotfoundPage.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", redirect: "/home" },
        { path: "/storymous-migration", redirect: "/home" },
        { path: "/home", component: HomePage },
        { path: "/user/:id", component: UserPage },
        { path: "/post/:id", component: PostPage },
        { path: "/:notFound(.*)", component: NotfoundPage } // regular expression for anything entered
    ],
});

export default router;