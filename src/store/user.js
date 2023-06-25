import axios from "axios";

// store/user.js
const state = {
    userData: null
  };
  
  const mutations = {
    SET_USER_DATA(state, userData) {
      state.userData = userData;
    }
  };
  
  const actions = {
    fetchUserData({ commit }) {
      // Make an API request to fetch the user data
      // Assuming you are using axios for HTTP requests
      axios
        .get('http://127.0.0.1:5000/user')
        .then(response => {
        const userData = response.data;
        commit('SET_USER_DATA', userData);
      }).catch(error => {
        console.error('Failed to fetch user data:', error);
      });
    }
  };
  
  const getters = {
    userPicture: state => state.userData ? state.userData.picture : null,
    username: state => state.userData ? state.userData.username : null,
    color: state => state.userData ? state.userData.color: null,
    nPosts: state => state.userData ? state.userData.nPosts : 0,
    nFollowers: state => state.userData ? state.userData.nFollowers : 0,
    nFollowing: state => state.userData ? state.userData.nFollowing : 0
  };
  
  export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters
  };
  