<template>
  <div class="bg" @click="$emit('close')"></div>
  <dialog open>
    <div class="dialog-div"> <b>Sign Up</b> </div>
    <span v-if="errorMessage" class="error-message">User already exists</span>
    <form @submit.prevent="submitForm">
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
            <span v-if="emailFocused" class="requirements" :class="requirementsValidEmail">Valid e-mail format</span>
        </div>
        <div class="form-control">
            <input 
            v-model="passOneValue" 
            :class="passOneClass" 
            @focus="passOneFocused = true" 
            @blur="passOneFocused = false" 
            id="password" name="password" type="password" ref="passwordInput" placeholder="Choose a password">
            <span v-if="passOneFocused" class="requirements" :class="requirementsPassOne">Contains min. 3 characters<br></span> 
        </div>
        <div class="form-control">
          <input 
          v-model="passTwoValue" 
          :class="passTwoClass"
          @focus="passTwoFocused = true" 
          @blur="passTwoFocused  = false" 
          id="repeatPassword" name="repeatPassword" type="password" ref="repeatPasswordInput" placeholder="Repeat password">
          <span v-if="passTwoFocused" class="requirements" :class="requirementsPassTwo">Passwords match</span>
          <span v-else class="requirements" :class="requirementsPassTwo"></span> 
        </div>
        <div>
            <button type="submit" class="button" :disabled="!validateForm()">
            <span v-if="!loading">Sign Up</span>
            <span v-else>
              <div class="lds-facebook"><div></div><div></div><div></div></div>
            </span>
            </button>
        </div>
        <div class="signup-message">Have an account already? <a href="" class="link" @click.prevent="$emit('signin')">Log In</a></div>
      </form>
  </dialog>
</template>

<script>
import SelectButton from "./SelectButton.vue";
import { mapActions } from "vuex";

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
      formValid: false,
      loading: false,
      errorMessage: false
    }
  },
  methods: {
    ...mapActions('auth', ['signup']), // Map the login action from the auth module
    validateForm() {
      const patternUsername = /^[A-Za-z0-9_]+$/;
      const patternEmail = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,})+$/;

      if (this.loading) {
          this.formValid = false;
          return false;
        } else if (
          (this.usernameValue.length >= 3) &&
          (this.usernameValue.length <= 20) &&
          patternUsername.test(this.usernameValue) &&
          patternEmail.test(this.emailValue) &&
          (this.passOneValue.length >= 3) &&
          (this.passTwoValue === this.passOneValue)
        ) {
          this.formValid = true;
          return true;
        } else {
          this.formValid = false;
          return false;
        }
    },
    submitForm() {
      const value = this.validateForm();
      if (value) {
        const credentials = {
          username: this.usernameValue,
          email: this.emailValue,
          password: this.passOneValue
        };
        this.loading = true;
        this.signup(credentials)
          .then(data => {
            // Handle the data here
            if (data.status === "Success") {
              this.loading = false;
              this.$emit('signin');
            }
          })
          .catch(error => {
            // Handle the error here
            this.errorMessage = true;
            this.loading = false;
            console.error('Registration failed:', error);
          });
        //this.$emit("close");
        window.scrollTo({
          top: 0,
          behavior: 'auto' // Use 'smooth' for smooth scrolling, or 'auto' for instant scrolling
        });
      }
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
    },
    emailClass() {
      const pattern = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,})+$/;
      if (this.emailValue.length === 0) {
        return "neutral-input"
      } else {
        if (pattern.test(this.emailValue) === true) {
          return "valid-input";
        } else {
          return "invalid-input";
        }
      }
    },
    requirementsValidEmail() {
      const pattern = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,})+$/;
      if (pattern.test(this.emailValue) === true) {
        return "valid-requirement";
      } else {
        return "invalid-requirement";
      }
    },
    passOneClass() {
      if (this.passOneValue.length === 0) {
        return "neutral-input"
      } else {
        if (this.passOneValue.length >= 3) {
          return "valid-input";
        } else {
          return "invalid-input";
        }
      }
    },
    requirementsPassOne() {
      if (this.passOneValue.length >= 3) {
        return "valid-requirement";
      } else {
        return "invalid-requirement";
      }
    },
    passTwoClass() {
      if (this.passTwoValue.length === 0) {
        return "neutral-input"
      } else {
        if (this.passTwoValue === this.passOneValue) {
          return "valid-input";
        } else {
          return "invalid-input";
        }
      }
    },
    requirementsPassTwo() {
      if (this.passTwoValue === this.passOneValue) {
        return "valid-requirement";
      } else {
        return "invalid-requirement";
      }
    }
  }
}

</script>

<style scoped>
.error-message {
  font-size: 15px;
  font-weight: bold;
  padding: 0 10px 0 10px;
  margin: 15px 0 -5px 0;
  color: rgb(255, 0, 0);
  align-self: center;
}

.lds-facebook {
  display: inline-block;
  position: relative;
  width: 40px;
  height: 40px;
}

.lds-facebook div {
  display: inline-block;
  position: absolute;
  left: 4px;
  width: 8px;
  background: #fff;
  animation: lds-facebook 1.2s cubic-bezier(0, 0.5, 0.5, 1) infinite;
}

.lds-facebook div:nth-child(1) {
  left: 4px;
  animation-delay: -0.12s;
}

.lds-facebook div:nth-child(2) {
  left: 16px;
  animation-delay: -0.06s;
}

.lds-facebook div:nth-child(3) {
  left: 28px;
  animation-delay: 0;
}

@keyframes lds-facebook {
  0% {
    top: 4px;
    height: 32px;
  }
  50%, 100% {
    top: 12px;
    height: 16px;
  }
}

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

.requirements {
  font-size: 12px;
  padding: 0 0 0 2px;
  margin: 0 0 0 0px;
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

.button {
  width: 100%;
  margin: auto;
  justify-content: center;
  align-items: center;
  padding: 10px 0;
  border-radius: 10px;
  border: 0;
  background-color: rgb(255, 174, 0);
  font-weight: bolder;
}
.button:hover {
  background-color: rgb(235, 160, 0);
  cursor: pointer;
}

.button[disabled] {
  width: 100%;
  margin: auto;
  justify-content: center;
  align-items: center;
  padding: 10px 0;
  border-radius: 10px;
  border: 0;
  background-color: rgb(255, 153, 0);
  font-weight: bolder;
  opacity: 0.6;
  cursor: default;
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