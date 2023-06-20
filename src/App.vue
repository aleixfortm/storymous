<template>
  <the-header></the-header>
  <block-frame>
    <top-message></top-message>
    <router-view></router-view>
  </block-frame>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";
import BlockFrame from "./components/layout/BlockFrame.vue";
import TopMessage from "./components/TopMessage.vue";

export default {
  components: {
    TheHeader,
    BlockFrame,
    TopMessage
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');

#app {
  font-family: 'IBM Plex Mono', monospace;
}

* {
  box-sizing: border-box;
}

html {
  font-family: "IBM Plex Mono", monospace;
  background-color: rgb(46, 54, 61);
}

body {
  margin: 0;
  position: relative;

}

.cur-def {
  cursor: default;
}

.cur-pnt {
  cursor: pointer;
}

</style>