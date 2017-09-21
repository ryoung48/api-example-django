import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// initial state
const state = {
    authorized: false,
    locked: false
}

// getters
const getters = {
    authorized: state => state.authorized,
    locked: state => state.locked
}

// mutations
const mutations = {
  setAuthorized(state, payload) {
    state.authorized = payload
  },
  setLock(state, payload) {
    state.locked = payload
  }
}

export default new Vuex.Store({
  state,
  getters,
  mutations
})
