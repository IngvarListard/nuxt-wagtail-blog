import { setContext } from 'apollo-link-context'
import { ApolloLink } from 'apollo-link'

export const middleware = ctx => {
  /**
   * По-умолчанию при рендере со стороны сервера заголовки не отправляются.
   * Добавление заголовков от клиента.
   */
  const ssrMiddleware = setContext((_, { headers }) => {
    if (process.client) return headers
    return {
      headers: {
        ...headers,
        connection: ctx.app.context.req.headers.connection,
        referer: ctx.app.context.req.headers.referer,
        cookie: ctx.app.context.req.headers.cookie
      }
    }
  })

  // Добавление CSRF-токена к запросу
  const csrfMiddleware = setContext((_, { headers }) => {
    return {
      headers: {
        ...headers,
        'X-CSRFToken': ctx.app.$cookies.get('csrftoken') || null
      }
    }
  })

  /**
   * Проверка статуса пользователя после каждого запроса.
   * Если пользовательская сессия закончилась, то выполняется очистка storage'a
   */
  const userStatusMiddleware = new ApolloLink((operation, forward) => {
    return forward(operation).map(response => {
      const userLoggedIn = ctx.app.$cookies.get('isLoggedIn')
      if (userLoggedIn) {
        const user = ctx.store.state.auth.user
        // TODO: проверить не будет ли данный подход генерить огромное количество зпросов
        if (!user.id) {
          ctx.store.dispatch('auth/getCurrentUser')
        }
      } else {
        ctx.store.mutate('auth/setUser')
      }
      return response
    })
  })

  const webSocketConnectionMiddleware = new ApolloLink((operation, forward) => {
    return forward(operation).map(response => {
      const userLoggedIn = ctx.app.$cookies.get('isLoggedIn')
      if (!userLoggedIn && ctx.store.socket.isConnected) {
      }
      return response
    })
  })

  return {
    ssrMiddleware,
    csrfMiddleware,
    userStatusMiddleware,
    webSocketConnectionMiddleware
  }
}
