//import axios from 'axios';
import router from '@/router'; // Import your Vue Router instance
import axios from "axios"

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
              const response = await axios.post('http://127.0.0.1:5000/login', credentials); // Replace '/api/login' with your actual API endpoint for login
              const data = response.data; // Assuming the API returns the user data upon successful login
              if (data.status == "success") {
                commit('SET_LOGGED_IN', true);
                commit('SET_USER', data.username);
                axios
                    .get(`http://127.0.0.1:5000/user/${data.username}`)
                    .then(response => {
                    const userData = response.data;
                    commit('SET_USER_DATA', userData);
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
        SET_USER_DATA(state, userData) {
          state.userData = userData;
        }
    },

    getters: {
        isLoggedIn: state => state.loggedIn,
        currentUser: state => state.user,
        userPicture: state => state.userData ? state.userData.picture : null,
        username: state => state.userData ? state.userData.username : null,
        color: state => state.userData ? state.userData.color: null,
        nPosts: state => state.userData ? state.userData.nPosts : 0,
        nFollowers: state => state.userData ? state.userData.nFollowers : 0,
        nFollowing: state => state.userData ? state.userData.nFollowing : 0
    }
}
