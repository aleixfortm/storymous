import axios from 'axios';

export const API_BASE_URL = 'http://192.168.1.44:5000';

// Retrieve the JWT token from local storage
const token = localStorage.getItem('jwtToken');

// Check if the token exists
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export default axios;