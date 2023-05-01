<template>
  <the-header></the-header>
  <block-frame>
    <router-view></router-view>
  </block-frame>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";
import BlockFrame from "./components/layout/BlockFrame.vue";


export default {
  components: {
    TheHeader,
    BlockFrame
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
  background-color: rgb(34, 40, 46);
}

body {
  margin: 0;
  position: relative;

}

</style>