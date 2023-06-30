import { createApp } from 'vue';
import router from "./router.js";
import App from './App.vue';
import store from './store'
import axios, { API_BASE_URL } from "./config.js"

const app = createApp(App);

app.use(store);
app.use(router);

function logoutUser() {
  store.commit('SET_LOGGED_IN', false);
  store.commit('SET_USER', null);
  store.commit("SET_USER_DATA", null);

  sessionStorage.clear();

  router.push('/home');
}

function checkTokenExpiration() {
  const token = sessionStorage.getItem('jwtToken');
  if (!token) {
    // Token does not exist, consider it expired
    return true;
  }
  const decodedToken = JSON.parse(atob(token.split('.')[1]));
  const expiration = decodedToken.exp * 1000; // Convert to milliseconds
  const currentTime = Date.now();
  return currentTime > expiration;
}

// Check if the JWT token and username exist in session storage
const token = sessionStorage.getItem('jwtToken');
const username = sessionStorage.getItem('username');

// Check if both token and username exist
if (token && username) {
  const isExpired = checkTokenExpiration();
  if (isExpired) {
    logoutUser();
  } else {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    store.commit('auth/SET_LOGGED_IN', true);
    store.commit("auth/SET_USER", username);

    axios
      .get(`${API_BASE_URL}/user/${username}`, { timeout: 5000 })
      .then(response => {
        store.commit('auth/SET_USER_DATA', response.data.user_data);
      })
      .catch(error => {
        if (axios.isCancel(error)) {
          console.error('Request timed out:', error);
        } else {
          console.error('Failed to fetch user data:', error);
        }
        logoutUser();
      });

    router.push('/home');
  }
}

app.mount('#app');
