// this file executes after every page refresh // ----------

import axios from 'axios';
import store from './store'

export const API_BASE_URL = 'https://aleixfortm.pythonanywhere.com/';

// Retrieve the JWT token and username from session storage
const token = sessionStorage.getItem('jwtToken');
const username = sessionStorage.getItem('username');

// Check if the token exists
if (token && username) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

  axios
    .get(`${API_BASE_URL}/user/${username}`)
    .then(response => {
        console.log(response.data.user_data)
        store.commit('auth/SET_USER_DATA', response.data.user_data);
    }).catch(error => {
        console.error('Failed to fetch user data:', error);
    })
}

export default axios;