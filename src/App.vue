<template>
  <the-header></the-header>
  <router-view></router-view>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";

export default {
  components: {
    TheHeader
  }
}
</script>

<style>
#app {
  width: 1000px;
  margin: auto;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
}
</style>
