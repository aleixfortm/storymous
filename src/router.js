import { createRouter, createWebHistory } from "vue-router";

import HomePage from "./pages/HomePage.vue";
import LoginPage from "./pages/LoginPage.vue";
import SignupPage from "./pages/SignupPage.vue";
import PostPage from "./pages/PostPage.vue";
import UserPage from "./pages/UserPage.vue";
import NotfoundPage from "./pages/NotfoundPage.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", redirect: "/home" },
        { path: "/home", component: HomePage },
        { path: "/login", component: LoginPage },
        { path: "/signup", component: SignupPage },
        { path: "/user/:id", component: UserPage },
        { path: "/post/:id", component: PostPage },
        { path: "/:notFound(.*)", component: NotfoundPage } // regular expression for anything entered
    ],
});

export default router;