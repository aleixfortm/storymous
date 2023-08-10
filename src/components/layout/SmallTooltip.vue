<template>
    <div v-if="condition" class="popup">{{ text }}</div>
</template>

<script>
export default {
    props: ["condition", "text"]
}
</script>

<style scoped>
.popup {
  position: absolute;
  top: 45px;
  transform: translateX(-25%);
  background-color: rgba(255, 255, 255, 0.95);
  padding: 5px;
  border-radius: 2px;
  font-size: 15px;
  text-align: start;
  z-index: 999;
  color: rgb(0, 0, 0);
  box-shadow: 0 0 20px 2px rgba(0, 0, 0, 0.5);
}

.popup::before {
  content: '';
  position: absolute;
  left: 50%;
  bottom: 100%;
  margin-left: -6px;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-bottom: 6px solid rgba(255, 255, 255, 0.95);
  z-index: 999;
}
</style>