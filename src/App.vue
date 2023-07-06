<template>
  <the-header></the-header>
  <block-frame>
    <router-view :key="$route.params.id"></router-view>
  </block-frame>
  <div class="marg-bot"></div>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";
import BlockFrame from "./components/layout/BlockFrame.vue";

export default {
  components: {
    TheHeader,
    BlockFrame,

  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');

.marg-bot {
  margin: 30px;
}

#app {
  font-family: 'IBM Plex Mono', monospace;
}

* {
  box-sizing: border-box;
}

html {
  font-family: "IBM Plex Mono", monospace;
  background-color: rgb(35, 42, 48);
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