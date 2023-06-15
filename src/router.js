import { createRouter, createWebHashHistory } from "vue-router";

import HomePage from "./pages/HomePage.vue";
import PostPage from "./pages/PostPage.vue";
import UserPage from "./pages/UserPage.vue";
//import NotfoundPage from "./pages/NotfoundPage.vue";

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: "/", redirect: "/storymous-migration/" },
        //{ path: "/storymous-migration", redirect: "/storymous-migration/home" },
        { path: "/storymous-migration/", component: HomePage },
        { path: "/storymous-migration/user/:id", component: UserPage },
        { path: "/storymous-migration/post/:id", component: PostPage },
        { path: "/:notFound(.*)", redirect: "/storymous-migration/" } // regular expression for anything entered
    ],
});

export default router;