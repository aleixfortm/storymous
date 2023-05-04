<template>
  <signin-dialog v-if="dialogShown === true && dialog === 'signin'" @close="toggleDialog" @signup="changeDialog('signup')" :key="'signin'"></signin-dialog>
  <signup-dialog v-else-if="dialogShown === true && dialog === 'signup'" @close="toggleDialog" @signin="changeDialog('signin')" :key="'signup'"></signup-dialog>
  <header>
      <nav>
          <div class="logo">
              <router-link to="/"><img src="../../assets/img/tree2.jpeg" alt="treelogo"></router-link>
              <h1><router-link to="/">Storymous</router-link></h1>
          </div>
          <search-bar></search-bar>
          <div class="login-div" v-if="!loggedIn">
            <button class="loginButton" @click="toggleDialog(); changeDialog('signin')">Log In</button>
          </div>
          <div v-else>
            <img src="../../assets/img/default_blue.png" alt="astronaut">
          </div>
      </nav>
  </header>

</template>


<script>
import SearchBar from "../SearchBar.vue";
import SigninDialog from "@/components/SigninDialog.vue";
import SignupDialog from "@/components/SignupDialog.vue";

export default {
  data() {
    return {
      loggedIn: false,
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
  }
};
</script>

<style scoped>

img {
  width: 50px;
  border-radius: 100px;
  padding: 2px 0 0 0;
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
}

h1 a:hover,
h1 a:active,
h1 a.router-link-active {
  border-color: transparent;
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