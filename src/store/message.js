export default {
    namespaced: true,
    state: {
        loginError: false
    },
    mutations: {
        // Mutation to set the loginError state to true
        SET_LOGIN_ERROR(state) {
        state.logInError = true;
        },
        // Mutation to set the loginError state to false
        RESET_LOGIN_ERROR(state) {
        state.logInError = false;
        }
    },
    actions: {
        // Action to trigger the SET_LOGIN_ERROR mutation
        setLoginError({ commit }) {
            if (!this.logInError) {
                commit('SET_LOGIN_ERROR');
                setTimeout(() => {
                    commit('RESET_LOGIN_ERROR');
                }, 3000)
            }

        },
    },
    getters: {
        // Getter to access the loginError state
        loginError(state) {
          return state.logInError;
        }
    }
};