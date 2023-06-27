import { createApp } from 'vue';
import router from "./router.js";
import App from './App.vue';
import store from './store'
import axios, { API_BASE_URL } from "./config.js"


const app = createApp(App);

app.use(store);
app.use(router);


// Check if the JWT token and username exist in session storage
const token = sessionStorage.getItem('jwtToken');
const username = sessionStorage.getItem('username');
//const userData = sessionStorage.getItem("userData")


// Check if both token and username exist
if (token && username) { // add userData if taking into account
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  // Set a flag or state variable indicating the user is logged in
  store.commit('auth/SET_LOGGED_IN', true);
  store.commit("auth/SET_USER", username);
  //store.commit("auth/SET_USER_DATA", userData)

  axios
    .get(`${API_BASE_URL}/user/${username}`, { timeout: 5000 })
    .then(response => {
        store.commit('auth/SET_USER_DATA', response.data.user_data);
    }).catch(error => {
        if (axios.isCancel(error)) {
            // Request timed out
            console.error('Request timed out:', error);
          } else {
            // Other error occurred
            console.error('Failed to fetch user data:', error);
          }
    });

  router.push('/');
}

app.mount('#app');