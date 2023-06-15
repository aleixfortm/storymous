import { createRouter, createWebHistory } from "vue-router";

import HomePage from "./pages/HomePage.vue";
import PostPage from "./pages/PostPage.vue";
import UserPage from "./pages/UserPage.vue";
//import NotfoundPage from "./pages/NotfoundPage.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", redirect: "/storymous-migration/home" },
        { path: "/storymous-migration", redirect: "/storymous-migration/home" },
        { path: "/storymous-migration/home", component: HomePage },
        { path: "/storymous-migration/user/:id", component: UserPage },
        { path: "/storymous-migration/post/:id", component: PostPage },
        { path: "/:notFound(.*)", redirect: "/storymous-migration/home" } // regular expression for anything entered
    ],
});

export default router;