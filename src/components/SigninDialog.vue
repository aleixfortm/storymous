<template>
  <div @click="$emit('close')"></div>
  <dialog open>
    <p>POLLANCRE LOL</p>
  </dialog>
</template>

<script>
export default {
  emits: ["close"]
}

</script>

<style scoped>
  div {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.75);
  z-index: 10;
}

dialog {
  position: fixed;
  display: flex;
  top: 20vh;
  margin: auto;
  z-index: 100;
  border-radius: 12px;
  border: none;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 0;
}

</style>