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


<style>
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
    color: #407be9;
}

button:active {
    border-bottom: 2px solid #407be9;
}

.flat {
    border-bottom: 2px solid #407be9;
}

.flat:hover,
.flat:active {
    background-color: #7b89a11e;
    color: #407be9;
}
</style>