const state = {
    emittedData: null,
  };
  
  const getters = {
    getEmittedData: (state) => state.emittedData,
  };
  
  const mutations = {
    SET_EMITTED_DATA(state, data) {
      state.emittedData = data;
    },
  };
  
  const actions = {
    emitData({ commit }, data) {
      commit("SET_EMITTED_DATA", data);
    },
  };
  
  export default {
    state,
    getters,
    mutations,
    actions,
  };