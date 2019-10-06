import Vue from 'vue'
import VueNativeSock from 'vue-native-websocket'

export default ({ store }, inject) => {
  const hostname =
    process.env.NODE_ENV === 'production'
      ? `${window.location.hostname}:${window.location.port}`
      : 'localhost:8000'
  Vue.use(VueNativeSock, `ws://${hostname}/ws/notifications/room1/`, {
    format: 'json',
    reconnection: true,
    reconnectionAttempts: 5,
    reconnectionDelay: 3000,
    store
  })
}
