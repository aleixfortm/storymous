<template>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
  <the-header></the-header>
  
  <block-frame>
    <router-view :key="$route.params.id"></router-view>
  </block-frame>

  <div class="marg-bot"></div>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";
import BlockFrame from "./components/layout/BlockFrame.vue";
import 'bootstrap/dist/css/bootstrap.css';
//import AlertMessage from "./components/layout/messages/AlertMessage.vue";

export default {
  components: {
    TheHeader,
    BlockFrame,
  //  AlertMessage
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');


.marg-bot {
  margin: 15px;
}

#app {
  font-family: 'IBM Plex Mono', monospace;
}

* {
  box-sizing: border-box;
  line-height: 1.2;
}

html {
  font-family: "IBM Plex Mono", monospace;
  background-color: rgb(35, 42, 48);
}

body {
  margin: 0;
  background-color: rgb(35, 42, 48);
}

.cur-def {
  cursor: default;
}

.cur-pnt {
  cursor: pointer;
}

</style>