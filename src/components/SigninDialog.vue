<template>
  <div class="bg" @click="$emit('close')"></div>
  <dialog open>
    <div class="dialog-div"> <b>Log In</b> </div>
    <div v-if="errorMessage" class="alert alert-danger m-0 mt-3" role="alert">
      Invalid credentials!
    </div>
    <form @submit.prevent="submitForm">
        <div class="form--control">
            <input v-model="usernameValue" id="title" name="title" type="text" ref="titleInput" placeholder="Username">
        </div>
        <div class="form--control">
          <input v-model="passwordValue" id="password" name="password" type="password" ref="passwordInput" placeholder="Password">
        </div>
        <div>
            <button class="button" :disabled="!validateForm()" type="submit" @click="scrollToTop">
            <span v-if="!loading">Log In</span>
            <span v-else>
              <div class="spinner-border spinner-border-sm" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            </span>
            </button>
        </div>
        <div class="signup-message">New to storymous? <a href="" @click.prevent="$emit('signup')" class="link">Sign Up</a></div>
      </form>
  </dialog>
</template>

<script>
import SelectButton from "./SelectButton.vue";
import { mapActions, mapGetters } from 'vuex';

export default {
  emits: ["close"],
  components: SelectButton,
  data() {
    return {
      formValid: false,
      usernameValue: "",
      passwordValue: "",
      loading: false,
      errorMessage: false
    }
  },
  methods: {
    ...mapActions('auth', ['login']), // Map the login action from the auth module
    validateForm() {

      if (this.loading) {
          this.formValid = false;
          return false;
        } else if (
          (this.usernameValue.length >= 3) && (this.passwordValue.length >= 3)
        ) {
          this.formValid = true;
          return true;
        } else {
          this.formValid = false;
          return false;
        }
    },
    submitForm() {
      this.validateForm();
      if (this.formValid) {
        const credentials = {
        // Obtain the entered credentials from the form
          username: this.usernameValue,
          password: this.passwordValue
        };
        this.loading = true;
        this.login(credentials)
          .then(data => {
            // Handle the data here
            if (data.status === "Success") {
              this.$emit('close');
            } else {
              this.loading = false;
              this.errorMessage = true;
            }
          })
          .catch(error => {
            // Handle the error here
            this.errorMessage = true;
            this.loading = false;
            console.error('Login failed:', error);
          });
        
        window.scrollTo({
          top: 0,
          behavior: 'auto' // Use 'smooth' for smooth scrolling, or 'auto' for instant scrolling
        });
      }
    },
  },
  computed: {
    ...mapGetters('auth', ['isLoggedIn', 'currentUser']),
    usernameChange() {
      return this.usernameValue;
    },
    passwordChange() {
      return this.passwordValue;
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
    border: 2px solid rgb(243, 243, 243);
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
  background-color: rgb(4, 255, 171);
  font-weight: bolder;
}

.button:hover {
  background-color: rgb(0, 233, 155);
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
  background-color: rgb(4, 255, 171);
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

.form--control {
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