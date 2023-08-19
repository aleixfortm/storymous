// store/modules/topData.js
export default {
    namespaced: true,
    state: {
      topAuthors: [],
      topStories: [],
    },
    mutations: {
      SET_TOP_AUTHORS(state, topAuthors) {
        state.topAuthors = topAuthors;
      },
      SET_TOP_STORIES(state, topStories) {
        state.topStories = topStories;
      },
    },
    actions: {
      saveTopData({ commit }, { topAuthors, topStories }) {
        commit('SET_TOP_AUTHORS', topAuthors);
        commit('SET_TOP_STORIES', topStories);
      },
    },
    getters: {
      topAuthors: state => state.topAuthors,
      topStories: state => state.topStories,
    },
  };
  