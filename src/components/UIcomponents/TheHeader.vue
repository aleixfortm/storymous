<template>
  <signin-dialog v-if="dialogShown === true && dialog === 'signin'" @close="toggleDialog" @signup="changeDialog('signup')" :key="'signin'"></signin-dialog>
  <signup-dialog v-else-if="dialogShown === true && dialog === 'signup'" @close="toggleDialog" @signin="changeDialog('signin')" :key="'signup'"></signup-dialog>
  <header>
      <nav>
          <div class="logo">
            <router-link class="logoimgcontainer" to="/"><img class="logoimg" src="@/assets/img/tree2.jpeg" alt="treelogo"></router-link>
            <router-link to="/" class="header-title">Storymous</router-link>
          </div>
          
          <div v-if="isLoggedIn === false" class="login-div">
            <div class="material-symbols-outlined user-select-none icon" @click="goHome">home</div>
            <!--
            <div class="material-symbols-outlined user-select-none icon" @click="showNotifications">search</div>
            -->
            <button class="loginButton" @click="toggleDialog(); changeDialog('signin')">Log In</button>
          </div>
          <div v-else class="options">
            <!--
            <div class="material-symbols-outlined user-select-none icon" @click="goHome">home</div>
            <div class="material-symbols-outlined user-select-none icon" @click="newstoryShown = !newstoryShown">search</div>
            -->
            <div class="icon-container-t" @mouseover="showSoonTooltip = true" @mouseout="showSoonTooltip = false">
              <div class="material-symbols-outlined user-select-none icon" @click="showNotifications">notifications</div>
              <small-tooltip :condition="showSoonTooltip" :text="'Coming soon!'" :top="'35px'" :transform="'translateX(10%)'"></small-tooltip>
            </div>
            
            <router-link :to="getProfileLink" class="userdata">
              <img class="userimg" v-if="userFetchedPicture" :src="imgSource" alt="astronaut">
              <img class="userimg" v-else src="@/assets/img/moon_default_avatar-min.png" alt="default avatar">
              <div class="user-data-container">
                <div class="name-container">
                  <div class="username">@{{ currentUser }}</div>
                </div>
                <div class="leave-container">
                  <div class="leave-data">
                    <span class="material-symbols-outlined custom-i">nest_eco_leaf</span>
                    <div class="leaves-num">{{ nFetchedLeaves }}</div>
                  </div>
                </div>
              </div>  
            </router-link>
          </div>
      </nav>
  </header>
</template>


<script>
import { mapGetters } from 'vuex';
import { useRouter } from 'vue-router';
import SigninDialog from "@/components/dialogs/SigninDialog.vue";
import SignupDialog from "@/components/dialogs/SignupDialog.vue";
import SmallTooltip from './SmallTooltip.vue';

export default {
  setup() {
        const router = useRouter();
        return { router: router };
    },
  data() {
    return {
      dialogShown: false,
      dialog: 'signin',
      newstoryShown: false,
      showSoonTooltip: false
    }
  },
  components: {
    SigninDialog,
    SignupDialog,
    SmallTooltip
  },
  methods: {
    toggleDialog() {
      this.dialogShown = !this.dialogShown;
    },
    changeDialog(dialog) {
      this.dialog = dialog;
    },
    goToProfile() {
      const ownUsername = this.currentUser;
      this.$router.push('/user/' + ownUsername);
    },
    goHome() {
      this.$router.push('/home');
    },
  },
  computed: {
      ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched", "nFetchedLeaves"]),
      getProfileLink() {
        return '/user/' + this.currentUser;
      },
      imgSource() {
            return require("@/assets/img/" + this.userFetchedPicture);
        }
  }
};
</script>

<style scoped>
.icon-container-t {
  position: relative;
  margin: 0;
}

.leaves-num {
  margin: 0 0 0 -2px;
}

.user-data-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin: 0;
}

.leave-container {
  margin: -2px 0 -2px 0;
}
.leave-data {
  display: flex;
  justify-content: left;
  align-items: left;
  margin: 0;
}

.name-container {
  display: flex;
  flex-direction: column;
  width: fit-content;
  margin: 0;
}

.icon {
  color: rgba(245, 245, 245, 0.877);
  position: relative;
  cursor: pointer;
  font-size: 24px;
  margin: 0 0 0 14px;
  transition: 0.1s all;
}

.icon:hover {
  color: rgba(245, 245, 245, 0.877);
  cursor: pointer;
  font-variation-settings:
  'FILL' 1,
  'wght' 300,
  'GRAD' 0,
  'opsz' 40
}

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 500,
  'GRAD' 0,
  'opsz' 48
}

.custom-i {
  height: fit-content;
  font-variation-settings:
  'FILL' 1,
  'wght' 200,
  'GRAD' -25,
  'opsz' 0
}


.options {
  display: flex;
  align-items: center;
  margin: 0 5px 0 5px;
}

.header-title {
  font-size: 26px;
  margin: 0 0 0 5px;
  color: rgb(0, 255, 149);
}

.header-title:hover {
  text-decoration: underline;
}

.logoimgcontainer {
  align-items: center;
  justify-content: center;
  margin: auto;
  height: 45px;
  border-radius: 500%;
}

.logoimg {
  height: 45px;
  border-radius: 500%;
  transition: 0.2s all;
}

.logoimg:hover {
  filter: brightness(85%);
}

.userdata {
  display: flex;
  padding: 1px 0px 1px 4px;
  font-family: inherit;
  color: rgb(0, 255, 98);
  cursor: pointer;
  font-size: 15px;
  width: fit-content;
  margin: 0 5px 0 10px;
  background-color: #ffffff1e;
  border-radius: 4px;
  align-items: center;
  transition: all 0.1s;
}

.userdata:hover {
  background-color: #adadad1e;
}

.username {
  height: fit-content;
  margin: 0 5px 0 5px;
  color: rgb(185, 221, 255);
  font-weight: bold;
}

.username:hover {
  text-decoration: underline;
}

.userimg {
  height: 35px;
  width: auto;
  border-radius: 100%;
}

div {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 20px;
}

.logo {
  align-items: center;
  margin: 0 5px 0 5px;
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
  background-color: #2b3830;
  background-color: #484945;
  border-bottom: rgba(0, 0, 0, 0.356) 1px solid;
  box-shadow: 0px 0px 5px 1px rgba(0, 0, 0, 0.445);
}

header a {
  text-decoration: none;
  color: rgb(4, 255, 171);
  display: inline-block;
  border: 1px solid transparent;
}


header nav {
  width: 800px;
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
  height: fit-content;
  padding: 5px 6px;
  font-family: inherit;
  border: 0px solid #e5e3ff;
  color: rgb(0, 255, 0);
  cursor: pointer;
  font-size: 15px;
  margin: 0 20px 0 20px;
  background-color: rgba(0, 145, 55, 0.726);
  border-radius: 4px;
  font-weight: bold;
  transition: all 0.2s;
}

.loginButton:hover {
    background-color: rgba(0, 128, 49, 0.452);
    color: rgb(0, 255, 98);
}

.login-div {
  height: 100%;
  margin: 0;
}

@media (max-width: 420px) {
  .header-title {
    display: none;
  }
}



</style>