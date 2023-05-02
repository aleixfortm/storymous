<template>
  <div class="bg" @click="$emit('close')"></div>
  <dialog open>
    <div class="dialog-div"> <b>Log In</b> </div>
    <form @submit.prevent="submitDataFunc()">
        <div class="form-control">
            <input id="title" name="title" type="text" ref="titleInput">
        </div>
        <div class="form-control">
          <input id="password" name="password" type="text" ref="passwordInput">
        </div>
        <div>
            <button type="submit">Log In</button>
        </div>
      </form>
  </dialog>
</template>

<script>
import SelectButton from "./SelectButton.vue";

export default {
  emits: ["close"],
  components: SelectButton
}

</script>

<style scoped>
label {
    font-weight: bold;
    display: block;
    margin-bottom: 0.5rem;
}

input {
    display: block;
    background-color: whitesmoke;
    width: 100%;
    font: inherit;
    padding: 0.15rem;
    border: 1px solid #ccc;
}

input:focus {
    outline: none;
    background-color: whitesmoke;
}

form {
  width: fit-content;
}

.form-control {
    margin: 1rem 0;
    width: 200px;
}

.bg {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.75);
  z-index: 10;
}

.dialog-div {
  text-align: start;
}

dialog {
  position: fixed;
  display: flex;
  flex-direction: column;
  top: 20vh;
  margin: auto;
  z-index: 100;
  border-radius: 12px;
  border: none;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 30px 50px;
  justify-content: center;
}

</style>