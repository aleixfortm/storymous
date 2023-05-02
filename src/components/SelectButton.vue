<template>
    <button :type="type" :class="mode">
        <slot></slot>
    </button>
</template>


<script>
export default {
  props: ["type", "mode"]
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
}

button:hover {
    background-color: #7b89a11e;
    color: rgb(4, 255, 150);
}

button:active {
    border-bottom: 2px solid rgb(4, 255, 150);
}

.flat {
    border-bottom: 2px solid rgb(4, 255, 150);
}

.flat:hover,
.flat:active {
    background-color: #7b89a11e;
    color: rgb(4, 255, 150);
}
</style>