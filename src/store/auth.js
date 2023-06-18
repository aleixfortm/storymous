//import axios from 'axios';
import router from '@/router'; // Import your Vue Router instance

export default {
    namespaced: true,

    state: {
        loggedIn: false,
        user: null,
    },

    actions: {
      /*
        async login({ commit }, credentials) {
            try {
              const response = await axios.post('http://192.168.1.44:5000/login', credentials); // Replace '/api/login' with your actual API endpoint for login
              const data = response.data; // Assuming the API returns the user data upon successful login
              if (data.status == "valid!") {
                commit('SET_LOGGED_IN', true);
                commit('SET_USER', data.username);
              }
              return data;
            } catch (error) {
              // Handle login error here, e.g., show an error message
              console.error('Login failed:', error);
            }
          },
          */
        login({ commit }, credentials) {
          const data = {
            status: "valid!",
            username: credentials._username
          }
          commit("SET_LOGGED_IN", true);
          commit("SET_USER", data.username)
        },
        logout({ commit }) {
          // Call your logout API here
          // If logout is successful, commit the mutations
          commit('SET_LOGGED_IN', false);
          commit('SET_USER', null);

          // Redirect the user to a different route
          router.push('/storymous-migration/'); // or router.replace('/somewhere-else');
        },
    },

    mutations: {
        SET_LOGGED_IN(state, isLoggedIn) {
            state.loggedIn = isLoggedIn;
          },
          SET_USER(state, user) {
            state.user = user;
          },
    },

    getters: {
        isLoggedIn: state => state.loggedIn,
        currentUser: state => state.user,
    }
}
