import axios from 'axios';

export default {
    namespaced: true,

    state: {
        loggedIn: false,
        user: null,
    },

    actions: {
        async login({ commit }, credentials) {
            try {
              const response = await axios.get('http://192.168.1.44:5000/ping', credentials); // Replace '/api/login' with your actual API endpoint for login
              const user = response.data; // Assuming the API returns the user data upon successful login
              console.log(user)
              //commit('SET_LOGGED_IN', true);
              commit('SET_USER', user);
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
