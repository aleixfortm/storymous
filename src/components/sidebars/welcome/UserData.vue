<template>
    <div @click="redirectToUser" class="userdata">
        <img class="userimg" v-if="user.picture" :src="imgSource" alt="astronaut">
        <img class="userimg" v-else src="@/assets/img/moon_default_avatar-min.png" alt="default avatar">
        <div class="user-data-container">
            <div class="name-container">
                <div class="username">@{{ user.username }}</div>
            </div>
            <div class="leave-container">
                <div class="leave-data">
                    <span class="material-symbols-outlined custom-i">nest_eco_leaf</span>
                    <div class="leaves-num">{{ user.leaves }}</div>
                </div>
            </div>
        </div>  
    </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
    props: ["user"],
    setup() {
        const router = useRouter();
        return { router: router };
    },
    computed: {
        imgSource() {
            return require("@/assets/img/" + this.user.picture)
        }
    },
    methods: {
      redirectToUser() {
        this.router.push(`/user/${this.user.username}`);
      }
    }
}
</script>

<style scoped>

.leaves-num {
  margin: 2px 0 0 -2px;
}
.custom-i {
    font-size: 22px;
  height: fit-content;
  font-variation-settings:
  'FILL' 1,
  'wght' 200,
  'GRAD' -25,
  'opsz' 0
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
.username:hover {
  text-decoration: underline;
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
.name-container {
  display: flex;
  flex-direction: column;
  width: fit-content;
  margin: 0;
}
.user-data-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin: 0;
}
.userimg {
  height: 35px;
  width: auto;
  border-radius: 100%;
}

.userdata {
  display: flex;
  padding: 4px 0px 4px 4px;
  font-family: inherit;
  color: rgb(0, 255, 98);
  cursor: pointer;
  font-size: 15px;
  width: fit-content;
  justify-content: flex-start;
  background-color: #ffffff09;
  width: 100%;
  border-radius: 4px;
  align-items: center;
  margin: 8px 0 0 0;
  transition: all 0.2s;
}
</style>