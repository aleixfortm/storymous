//import axios from 'axios';
import router from '@/router'; // Import your Vue Router instance
import axios from "../../config"
import { API_BASE_URL } from '../../config';

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
            //try to log in with credentials and retrieve user data from response
            const response = await axios.post(`${API_BASE_URL}/login`, credentials);
            const data = response.data;
            // if status is successful, continue with assigning credentials to user
            if (data.status == "Success") {
              // set state variables as logged in and username
              commit('SET_LOGGED_IN', true);
              commit('SET_USER', data.user_data.username);
              // save token and username on session storage
              const token = data.token;
              const userData = data.user_data;
              sessionStorage.setItem('username', userData.username); // Store username in session storage
              sessionStorage.setItem('jwtToken', token); // Store the JWT token in session storage
              // save user data on state variables
              commit('SET_USER_DATA', userData);
        
              // Set the JWT token in the axios default headers for subsequent requests
              axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

              router.push("/home")
              
              return data;
            }
          } catch (error) {
            // Handle login error here, e.g., show an error message
            console.error('Login failed:', error);
          }
        },
        async signup({ commit }, stuff) {
          try {
            const response = await axios.post(`${API_BASE_URL}/signup`, stuff);
            const data = response.data

            if (data.status == "Success") {

              commit('SET_LOGGED_IN', false);
              return data;
            }
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
          commit("SET_USER_DATA", null)

          sessionStorage.clear();

          router.push('/');
        },
        async followUser({ commit }, userToFollow) {
          try {
            commit('ADD_USER_TO_FOLLOWING', userToFollow);
          } catch (error) {
            console.error('Error unfollowing user:', error);
          }
        },
        async unfollowUser({ commit }, userToUnfollow) {
          try {
            commit('REMOVE_USER_FROM_FOLLOWING', userToUnfollow);
          } catch (error) {
            console.error('Error unfollowing user:', error);
          }
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
        },
        ADD_USER_TO_FOLLOWING(state, user) {
          state.userData.following.push(user);
        },
        REMOVE_USER_FROM_FOLLOWING(state, user) {
          const userIndex = state.userData.following.indexOf(user);
          if (userIndex !== -1) {
            state.userData.following.splice(userIndex, 1);
          }
        },
        
    },

    getters: {
        isLoggedIn: state => state.loggedIn,
        currentUser: state => state.user,
        userFetchedPicture: state => state.userData ? state.userData.picture : null,
        userFetchedBio: state => state.userData ? state.userData.bio : null,
        colorFetched: state => state.userData ? state.userData.color: null,
        nFetchedPosts: state => state.userData ? state.userData.started_stories + state.userData.continued_stories : 0,
        nFetchedFollowers: state => state.userData ? state.userData.followers : [],
        nFetchedFollowing: state => state.userData ? state.userData.following : [],
        nFetchedLeaves: state => state.userData ? state.userData.leaves : 0,
    }
}
