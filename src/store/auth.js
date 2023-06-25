//import axios from 'axios';
import router from '@/router'; // Import your Vue Router instance
import axios from "axios"
import { API_BASE_URL } from '@/config';

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
              const response = await axios.post(`${API_BASE_URL}/login`, credentials); // Replace '/api/login' with your actual API endpoint for login
              const data = response.data; // Assuming the API returns the user data upon successful login
              if (data.status == "success") {
                commit('SET_LOGGED_IN', true);
                commit('SET_USER', data.username);
                axios
                    .get(`http://83.44.90.168:8001/user/${data.username}`)
                    .then(response => {
                      const userFetchedData = response.data.userdata;
                      console.log(userFetchedData)
                      commit('SET_USER_DATA', userFetchedData);
                  }).catch(error => {
                    console.error('Failed to fetch user data:', error);
                  });
                }
              return data;
            } catch (error) {
              // Handle login error here, e.g., show an error message
              console.error('Login failed:', error);
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
