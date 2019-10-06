/* eslint-disable no-console */
import Vue from 'vue'
import { generateUid } from '@/utils'

export const state = () => ({
  errors: [],
  notifications: [],
  socket: {
    isConnected: false,
    message: '',
    reconnectError: false
  }
})

export const mutations = {
  pushError({ errors }, error) {
    errors.push(error)
  },
  shiftError: ({ errors }) => errors.shift(),
  hideError({ errors }, id) {
    const error = errors.find(e => e.id === id)
    if (error) {
      error.show = false
    }
  },
  showError({ errors }, id) {
    const error = errors.find(e => e.id === id)
    if (error) {
      error.show = true
    }
  },
  SOCKET_ONOPEN(state, event) {
    Vue.prototype.$socket = event.currentTarget
    state.socket.isConnected = true
    console.log('opened')
  },
  SOCKET_ONCLOSE(state, event) {
    state.socket.isConnected = false
    console.log('closed')
  },
  SOCKET_ONERROR(state, event) {
    console.error(state, event)
    console.log('error')
  },
  // default handler called for all methods
  SOCKET_ONMESSAGE(state, message) {
    state.socket.message = message.message
    console.log('message: ', message.message)
  },
  // mutations for reconnect methods
  SOCKET_RECONNECT(state, count) {
    console.info(state, count)
  },
  SOCKET_RECONNECT_ERROR(state) {
    state.socket.reconnectError = true
  }
}

export const getters = {
  errorsGetter: ({ errors }) => errors
}

export const actions = {
  pushError(ctx, error) {
    const id = generateUid()
    ctx.commit('pushError', { id, text: error, show: false })
    setTimeout(() => {
      ctx.commit('showError', id)
    }, 50)
    setTimeout(() => {
      ctx.commit('hideError', id)
    }, 5000)
  },
  async nuxtServerInit({ dispatch }, ctx) {
    const isLoggedIn = ctx.app.$cookies.get('isLoggedIn')
    if (isLoggedIn) {
      await dispatch('auth/getCurrentUser')
    }
  }
}
