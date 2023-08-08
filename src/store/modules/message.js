export default {
    namespaced: true,
    state: {
        loginError: false
    },
    mutations: {
        // Mutation to set the loginError state to true
        SET_LOGIN_ERROR(state) {
        state.loginError = true;
        },
        // Mutation to set the loginError state to false
        RESET_LOGIN_ERROR(state) {
        state.loginError = false;
        }
    },
    actions: {
        setLoginError({ commit }) {
            if (!this.loginError) {
                commit('SET_LOGIN_ERROR');
                setTimeout(() => {
                    commit('RESET_LOGIN_ERROR');
                }, 2500)
            }

        },
    },
    getters: {
        // Getter to access the loginError state
        loginError(state) {
          return state.loginError;
        }
    }
};