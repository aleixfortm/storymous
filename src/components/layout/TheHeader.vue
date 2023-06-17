<template>
  <signin-dialog v-if="dialogShown === true && dialog === 'signin'" @close="toggleDialog" @signup="changeDialog('signup')" :key="'signin'"></signin-dialog>
  <signup-dialog v-else-if="dialogShown === true && dialog === 'signup'" @close="toggleDialog" @signin="changeDialog('signin')" :key="'signup'"></signup-dialog>
  <header>
      <nav>
          <div class="logo">
              <router-link class="logoimgcontainer" to="/"><img class="logoimg" src="../../assets/img/logo.png" alt="treelogo"></router-link>
              <h1><router-link to="/storymous-migration/home">Storymous</router-link></h1>
          </div>
          <search-bar></search-bar>
          <div v-if="isLoggedIn === false" class="login-div">
            <button class="loginButton" @click="toggleDialog(); changeDialog('signin')">Log In</button>
          </div>
          <div v-else class="userdata">
              <div class="username">@{{ currentUser }}</div>
              <img class="userimg" src="../../assets/img/default_blue.png" alt="astronaut">
          </div>
      </nav>
  </header>

</template>


<script>
import { mapGetters } from 'vuex';

import SearchBar from "../SearchBar.vue";
import SigninDialog from "@/components/SigninDialog.vue";
import SignupDialog from "@/components/SignupDialog.vue";

export default {
  data() {
    return {
      dialogShown: false,
      dialog: 'signin'
    }
  },
  components: {
    SearchBar,
    SigninDialog,
    SignupDialog
  },
  methods: {
    toggleDialog() {
      this.dialogShown = !this.dialogShown;
    },
    changeDialog(dialog) {
      this.dialog = dialog;
    }
  },
  computed: {
      ...mapGetters('auth', ['isLoggedIn', 'currentUser']),
  }
};
</script>

<style scoped>
  .no-underline {
    text-decoration: none;
  }

.logo {
  align-items: center;
}

.logoimgcontainer {
  align-items: center;
  justify-content: center;
  margin: auto;
  height: auto;
}

.logoimg {
  height: 45px;
  border-radius: 10px;
  margin: 7px 0px 0 0;
}

.userdata {
  padding: 0 5px 0 5px;
  height: 50px;
  font-family: inherit;
  color: rgb(0, 255, 98);
  cursor: pointer;
  font-size: 15px;
  width: fit-content;
  margin: 0 5px 0 20px;
  background-color: #ffffff1e;
  border-radius: 4px;
}

.userdata:hover {
  background-color: #adadad1e;
}

.username {
  height: 50px;
  margin: 0 10px 0 10px;
  color: rgb(185, 221, 255);
  font-weight: bold;
}

.username:hover {
  text-decoration: underline;
}

.userimg {
  height: 85%;
  width: auto;
  border-radius: 100%;
}

div {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 20px;
}

header {
  position: fixed;
  z-index: 100;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  margin: 0;
  width: 100%;
  height: 3.5rem;
  background-color: #435055;
}

header a {
  text-decoration: none;
  color: rgb(4, 255, 171);
  display: inline-block;
  border: 1px solid transparent;
}

a:active,
a:hover,
a.router-link-active {
  color: rgb(4, 255, 171);
}

h1 {
  margin: 0;
}

h1 a {
  color: rgb(4, 255, 150);
  margin: 0 0 0 5px;
  text-decoration: none;
}

h1 a:hover,
h1 a:active,
h1 a.router-link-active {
  border-color: transparent;
  text-decoration: underline;
}

header nav {
  width: 100%;
  height: 100%;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header ul {
  list-style: none;
  margin: 0;
  padding: 5px 0;
  justify-content: center;
  align-items: center;
  width: fit-content;
}

li {
  width: fit-content;
  height: fit-content;
}

.loginButton {
  padding: 0;
  width: fit-content;
  height: 65%;
  font-family: inherit;
  border: 0px solid #e5e3ff;
  color: rgb(0, 255, 98);
  cursor: pointer;
  font-size: 15px;
  width: 80px;
  margin: 0 20px 0 20px;
  background-color: #ffffff1e;
  border-radius: 4px;
}

.loginButton:hover {
    background-color: #a5a5a51e;
    color: rgb(0, 255, 55);
}

.login-div {
  height: 100%;
  margin: 0;
}

@media (max-width: 500px) {
  h1 {
    display: none;
  }
}

</style>