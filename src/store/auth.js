//import axios from 'axios';
import router from '@/router'; // Import your Vue Router instance
import axios from "../config"
import { API_BASE_URL } from '../config';

export default {
    namespaced: true,

    state: {
        loggedIn: false,
        user: null,
        userData: null
    },

    actions: {
        async login({ commit }, credentials) {
          try {
            const response = await axios.post(`${API_BASE_URL}/login`, credentials);
            const data = response.data;
            if (data.status == "Success") {
              commit('SET_LOGGED_IN', true);
              commit('SET_USER', data.user_data.username);
        
              const token = data.token;
              const userData = data.user_data;
              console.log(userData);
        
              commit('SET_USER_DATA', userData);
        
              sessionStorage.setItem('username', userData.username); // Store username in session storage
              sessionStorage.setItem('jwtToken', token); // Store the JWT token in session storage
              sessionStorage.setItem("userData", userData);
        
              // Set the JWT token in the axios default headers for subsequent requests
              axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        
              return data;
            }
          } catch (error) {
            console.log(error);
          }
        },
        logout({ commit }) {
          // Call your logout API here
          // If logout is successful, commit the mutations
          commit('SET_LOGGED_IN', false);
          commit('SET_USER', null);

          router.push('/storymous/');
        },
    },

    mutations: {
        SET_LOGGED_IN(state, isLoggedIn) {
            state.loggedIn = isLoggedIn;
        },
        SET_USER(state, user) {
          state.user = user;
        },
        SET_USER_DATA(state, userFetchedData) {
          state.userData = userFetchedData;
        }
    },

    getters: {
        isLoggedIn: state => state.loggedIn,
        currentUser: state => state.user,
        userFetchedPicture: state => state.userData ? state.userData.picture : null,
        userFetchedBio: state => state.userData ? state.userData.bio : null,
        colorFetched: state => state.userData ? state.userData.color: null,
        nFetchedPosts: state => state.userData ? state.userData.n_writ_posts : 0,
        nFetchedFollowers: state => state.userData ? state.userData.followers.length : 0,
        nFetchedFollowing: state => state.userData ? state.userData.following.length : 0
    }
}
