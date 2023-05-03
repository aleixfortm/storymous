<template>
  <div class="bg" @click="$emit('close')"></div>
  <dialog open>
    <div class="dialog-div"> <b>Sign up</b> </div>
    <form @submit.prevent="submitDataFunc()">
        <div class="form-control">
            <input 
            v-model="usernameValue"
            :class="usernameClass" 
            @focus="usernameFocused = true" 
            @blur="usernameFocused = false" 
            id="username" 
            name="username" 
            type="text" 
            ref="usernameInput" 
            placeholder="Choose a username">
            <span v-if="usernameFocused" class="requirements" :class="requirementsCharcount">Contains between 3-20 characters<br></span> 
            <span v-if="usernameFocused" class="requirements" :class="requirementsSpecial">No special characters (_ allowed)</span>
        </div>
        <div class="form-control">
            <input 
            v-model="emailValue" 
            :class="emailClass" 
            @focus="emailFocused = true" 
            @blur="emailFocused = false"
            id="email" name="email" type="text" ref="emailInput" placeholder="Your e-mail">
            <span v-if="emailFocused" class="requirements">Valid e-mail format</span>
        </div>
        <div class="form-control">
            <input 
            v-model="passOneValue" 
            :class="passOneClass" 
            @focus="passOneFocused = true" 
            @blur="passOneFocused = false" 
            id="password" name="password" type="password" ref="passwordInput" placeholder="Choose a password">
            <span v-if="passOneFocused" class="requirements">Contains min. 3 characters<br></span> 
        </div>
        <div class="form-control">
          <input 
          v-model="passTwoValue" 
          :class="passTwoClass"
          @focus="passTwoFocused = true" 
          @blur="passTwoFocused  = false" 
          id="repeatPassword" name="repeatPassword" type="password" ref="repeatPasswordInput" placeholder="Repeat password">
          <span v-if="passTwoFocused" class="requirements">Passwords match<br></span> 
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
  components: SelectButton,
  data() {
    return {
      usernameValue: '',
      usernameFocused: false,
      emailValue: '',
      emailFocused: false,
      passOneValue: '',
      passOneFocused: false,
      passTwoValue: '',
      passTwoFocused: false,
    }
  },
  computed: {
    usernameClass() {
      var usernameLength = this.usernameValue.length;
      if (usernameLength === 0) {
        return "neutral-input";
      } else if (usernameLength >= 3 && usernameLength <= 20) {
        return "valid-input";
      } else {
        return "invalid-input";
      }
    },
    requirementsCharcount() {
      var usernameLength = this.usernameValue.length;
      if (usernameLength >= 3 && usernameLength <= 20) {
        return "valid-requirement";
      } else {
        return "invalid-requirement";
      }
    },
    requirementsSpecial() {
      const pattern = /^[A-Za-z0-9_]+$/;
      if ((pattern.test(this.usernameValue) || this.usernameValue === '') === true) {
        return "valid-requirement";
      } else {
        return "invalid-requirement";
      }
    }
  }
}

</script>

<style scoped>
.valid-input {
  border: 1px solid rgb(0, 214, 82);
}

.invalid-input {
  border: 1px solid red;
}

.neutral-input {
  border: 1px solid rgb(243, 243, 243);
}

.valid-requirement {
  color: rgb(0, 177, 68);
}

.invalid-requirement {
  color: red;
}

.hidden {
  display: none;
  height: 0;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.requirements {
  font-size: 12px;
  padding: 0 0 0 6px;
  margin: 0 0 0 5px;
  font-weight: bold;
}

label {
    font-weight: bold;
    display: block;
    margin-bottom: 0.5rem;
}

input {
    display: block;
    background-color: rgb(243, 243, 243);
    width: 100%;
    font: inherit;
    padding: 0.7rem 1rem;
    border: 2px solid rgb(243, 243, 243);
    border-radius: 8px;
}

input:focus {
    outline: none;
    background-color: rgb(243, 243, 243);
    color: rgb(53, 53, 53);
}

input:active {
    background-color: rgb(243, 243, 243);
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
  cursor: pointer;
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
  padding: 0 0 0 4px;
  font-size: 24px;
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