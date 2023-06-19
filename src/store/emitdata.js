export default {
  namespaced: true,

  state: {
    emittedData: null,
  },

  actions: {
    emitData({ commit }, data) {
      commit("SET_EMITTED_DATA", data);
    }
  },

  mutations: {
    SET_EMITTED_DATA(state, data) {
      state.emittedData = data;
    }
  },

  getters: {
    getEmittedData: (state) => state.emittedData,
  },
}
