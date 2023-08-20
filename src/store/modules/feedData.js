// store/modules/feedData.js

export default {
    namespaced: true,
    state: {
      latestPosts: [],
      followingPosts: [],
    },
    mutations: {
      SET_LATEST_POSTS(state, posts) {
        state.latestPosts = posts;
      },
      SET_FOLLOWING_POSTS(state, posts) {
        state.followingPosts = posts;
      },
    },
    actions: {
      setLatestPosts({ commit }, posts) {
        commit('SET_LATEST_POSTS', posts);
      },
      setFollowingPosts({ commit }, posts) {
        commit('SET_FOLLOWING_POSTS', posts);
      },
    },
    getters: {
      latestPosts: state => state.latestPosts,
      followingPosts: state => state.followingPosts,
    },
  };