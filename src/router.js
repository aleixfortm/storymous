import { createRouter, createWebHistory } from "vue-router";

import HomePage from "./pages/HomePage.vue";
import PostPage from "./pages/PostPage.vue";
import UserPage from "./pages/UserPage.vue";
import NewPost from "./pages/NewPost.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", redirect: "/storymous-migration/" },
        { path: "/storymous-migration/", component: HomePage },
        { path: "/storymous-migration/newpost", component: NewPost },
        { path: "/storymous-migration/user/:id", component: UserPage },
        { path: "/storymous-migration/post/:id", component: PostPage },
        { path: "/storymous-migration/:catchAll(.*)", redirect: "/storymous-migration/" } // named redirect route for any undefined route
    ],
});

export default router;