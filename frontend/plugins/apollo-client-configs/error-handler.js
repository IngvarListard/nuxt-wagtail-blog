import { onError } from 'apollo-link-error'

export const errorLink = ctx =>
  onError(({ graphQLErrors }) => {
    if (!graphQLErrors || graphQLErrors.length === 0) return
    let text = graphQLErrors[0].message
    if (text === '') {
      return
    }
    if (text.indexOf('matching query does not exist') > 0) {
      ctx.error('Страница не найдена')
      return
    }
    if (text.indexOf('::') > -1) {
      const split = text.split('::', 2)
      text = split[1] || ''
      const code = parseInt(split[0])
      if (code === 401 && ctx.route.name && ctx.route.name !== 'login') {
        // Необходим логин
        const currentRoute = ctx.route.path
        ctx.next({
          path: '/login',
          query: { redirect: currentRoute }
        })
        return
      }
      if (ctx.route.path === '/') {
        return
      }
    }
    const length = ctx.store.state.errors.length
    const last = length > 0 ? ctx.store.state.errors[length - 1] : null
    if (last && last.text === text && last.show) {
      return
    }
    ctx.store.dispatch('pushError', text)
    if (ctx.store.state.errors.length > 5) {
      ctx.store.commit('shiftError')
    }
  })
