export default {
  namespaced: true,
  state: {
    contributors: [],
    newStatus: false
  },
  mutations: {
    SET_CONTRIBUTORS(state, contributors) {
      state.contributors = contributors;
    },
    SET_NEW_STATUS(state, status) {
      state.newStatus = status;
    }
  },
  actions: {
    setContributors({ commit }, contributors) {
      commit('SET_CONTRIBUTORS', contributors);
    },
    setNewStatus({ commit }, status) {
      commit('SET_NEW_STATUS', status);
    }
  },
  getters: {
    getContributors: state => state.contributors,
    getNewStatus: state => state.newStatus
  }
};
