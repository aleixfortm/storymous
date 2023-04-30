<template>
  <the-header></the-header>
  <the-block>
    <router-view></router-view>
  </the-block>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";
import TheBlock from "./components/layout/TheBlock.vue";

export default {
  components: {
    TheHeader,
    TheBlock
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
}

body {
  margin: 0;
  position: relative;
}

</style>
