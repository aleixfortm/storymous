<template>
    <button :type="type" :class="[mode, { selected }]">
        <slot></slot>
    </button>
</template>


<script>
export default {
  props: ["type", "mode", "selected"]
}
</script>


<style scoped>
div {
  width: 60%;
  height: 100%;
  align-items: center;
  justify-content: center;
  padding: 6px 0 0 0;
  margin: 0 auto;
}

button {
  width: 100%;
  height: 100%;
  font-family: inherit;
  background-color: #5130ad00;
  border: 0px solid #e5e3ff;
  color: white;
  cursor: pointer;
  font-size: 25px;
  transition: 0.2s all;
}

button:hover {
    background-color: #7b89a11e;
}

button:active {
  background-color: rgba(255, 255, 255, 0);
}

.flat {
    border-bottom: 2px solid rgb(4, 255, 150);
    transition: 0.3s all;
}

.flat:hover,
.flat:active {
    background-color: #7b89a11e;
}

.null {
  border-bottom: 2px solid rgba(158, 158, 158, 0.055);
  transition: 0.3s all;
}

.null:active {
  border-bottom: 2px solid rgb(255, 255, 255);
}

button.selected:hover {
  background-color: #5130ad00;
}
</style>