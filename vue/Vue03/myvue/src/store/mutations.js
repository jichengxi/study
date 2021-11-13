import vue from 'vue'

const mutations = {
  SET_APP_NAME (state, params) {
    console.log(params)
    state.appName = params
  },
  SET_APP_VERSION (state) {
    vue.set(state, 'appVersion', 'v1.0')
  },
  SET_STATE_VALUE (state, value) {
    console.log(value)
    state.stateValue = value
  }
}
export default mutations
