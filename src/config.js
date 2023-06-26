import axios from 'axios';
import store from './store'

export const API_BASE_URL = 'http://192.168.1.44:5000';

// Retrieve the JWT token and username from session storage
const token = sessionStorage.getItem('jwtToken');
const username = sessionStorage.getItem('username');

// Check if the token exists
if (token && username) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  console.log(token)
  console.log(username)

  axios
    .get(`${API_BASE_URL}/user/${username}`)
    .then(response => {
        store.commit('auth/SET_USER_DATA', response.data.userdata);
    }).catch(error => {
        console.error('Failed to fetch user data:', error);
    })
}

export default axios;