/* eslint-disable no-console */
import { Promise } from 'q'
import { LOGIN, LOGOUT } from '@/graphql/users/mutations'
import { GET_CURRENT_USER } from '@/graphql/users/queries'

function apollo(ctx) {
  return ctx.app.apolloProvider.defaultClient
}

export const state = () => ({
  user: {
    id: null,
    firstName: null,
    lastName: null,
    loggedIn: false,
    email: null,
    isActive: false,
    permissions: []
  }
})

export const mutations = {
  setUser(state, user) {
    if (user) {
      Object.assign(state.user, user)
      state.user.loggedIn = true
    } else {
      Object.assign(state.user, {
        id: null,
        firstName: null,
        lastName: null,
        email: null,
        isActive: null,
        loggedIn: false
      })
    }
  }
}

export const actions = {
  login(ctx, { login, password }) {
    return apollo(this)
      .mutate({
        mutation: LOGIN,
        variables: { login, password }
      })
      .then(({ data }) => {
        ctx.commit('setUser', data.login.user)
      })
  },
  logout(ctx) {
    return apollo(this)
      .mutate({
        mutation: LOGOUT
      })
      .then(({ data }) => {
        if (data.logout.success) {
          ctx.commit('setUser')
        }
      })
  },
  register(ctx) {
    return new Promise()
  },
  changePassword(ctx) {
    return new Promise()
  },
  /**
   * Из этого запроса данные о CURRENT USER попадают
   * в кэш Apollo, и далее они доступны повсеместно
   * с помощью запроса CURRENT_USER_CLIENT.
   * В идеале, функционал auth лучше полностью перенести
   * на плечи apollo.
   */
  getCurrentUser(ctx) {
    // из этого запроса данные о CURRENT USER
    return apollo(this)
      .query({
        query: GET_CURRENT_USER,
        fetchPolicy: 'network-only'
      })
      .then(({ data }) => {
        ctx.commit('setUser', data.getCurrentUser)
      })
  },
  getPermissions(ctx) {
    return new Promise()
  }
}

export const getters = {
  hasPerm: state => perm => {
    return !!state.user.permissions.find(permission => perm === permission)
  }
}
