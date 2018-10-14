import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    users: []
  },
  mutations: {
    setUsers (state, payload) {
      state.users = payload
    }
  },
  actions: {
    async getUsers ({ commit }) {
      const response = await axios.get('http://localhost:8000/api/user/json/')
      const users = response.data.data.map(item => {
        return {
          'username': item.username,
          'email': item.email
        }
      })
      commit('setUsers', users)
    }
  }
})
