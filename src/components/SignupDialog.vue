<template>
  <div class="bg" @click="$emit('close')"></div>
  <dialog open>
    <div class="dialog-div"> <b>Sign up</b> </div>
    <form @submit.prevent="submitDataFunc()">
        <div class="form-control">
            <input id="username" name="username" type="text" ref="usernameInput" placeholder="Choose a username">
        </div>
        <div class="form-control">
            <input id="email" name="email" type="text" ref="emailInput" placeholder="Your e-mail">
        </div>
        <div class="form-control">
            <input id="password" name="password" type="text" ref="passwordInput" placeholder="Choose a password">
        </div>
        <div class="form-control">
          <input id="repeatPassword" name="repeatPassword" type="text" ref="repeatPasswordInput" placeholder="Repeat password">
        </div>
        <div>
            <button type="submit">Sign Up</button>
        </div>
        <div class="signup-message">Have an account already? <a href="" class="link" @click.prevent="$emit('signin')">Log In</a></div>
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
    padding: 1rem;
    border: 2px solid whitesmoke;
}

input:focus {
    outline: none;
    background-color: whitesmoke;
    color: rgb(53, 53, 53);
}

input:active {
    background-color: whitesmoke;
    color: rgb(53, 53, 53);
}

input::placeholder {
    color: rgb(109, 109, 109);
    font-size: 14px;
}

form {
  outline: 0;
  width: fit-content;
}

button {
  width: 100%;
  margin: auto;
  justify-content: center;
  align-items: center;
  padding: 10px 0;
  border-radius: 10px;
  border: 0;
  background-color: rgb(155, 215, 255);
  font-weight: bolder;
}

button:hover {
  background-color: rgb(103, 194, 255);
}

.link {
  color: rgb(0, 81, 255);
}

.link:hover {
  color: rgb(0, 58, 182);
}

.signup-message {
  margin: 10px 0 0 0;
  font-size: 13px;
  font-weight: bold;
}

.form-control {
    margin: 1rem 0;
    width: auto;
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