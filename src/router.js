import { createRouter, createWebHistory } from "vue-router";

import HomePage from "./pages/HomePage.vue";
import PostPage from "./pages/PostPage.vue";
import UserPage from "./pages/UserPage.vue";
import NewPost from "./pages/NewPost.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", redirect: "/storymous/" },
        { path: "/storymous/", component: HomePage },
        { path: "/storymous/home", redirect: "/storymous/" },
        { path: "/storymous/newpost", component: NewPost },
        { path: "/storymous/user/:id", component: UserPage },
        { path: "/storymous/post/:id", component: PostPage },
        { path: "/storymous/:catchAll(.*)", redirect: "/storymous/" } // named redirect route for any undefined route
    ],
});

export default router;