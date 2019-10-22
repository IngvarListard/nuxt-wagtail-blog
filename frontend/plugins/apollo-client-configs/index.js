import { from, split, concat } from 'apollo-link'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { isSubscription } from '../../utils'
import { cacheRedirects } from '../../graphql/localSchema'
import { errorLink as errorHandler } from './error-handler'
import { middleware } from './middleware'
import { httpLink as buildedHttpLink } from './build-http-link'
import { wsLink } from './build-ws-link'
import { uploadLink } from './build-upload-link'
import { typeDefs, resolvers } from './local-schema'
import { fragmentMatcher } from './fragmentMatcher'

export default ctx => {
  const {
    ssrMiddleware,
    csrfMiddleware,
    userStatusMiddleware,
    webSocketConnectionMiddleware
  } = middleware(ctx)
  const errorLink = errorHandler(ctx)

  // Если загружается файл, то используем uploadLink
  let httpLink = split(
    operation => operation.getContext().hasUpload,
    uploadLink,
    buildedHttpLink
  )

  // Если тип операции subsctiption, то используем wsLink
  httpLink = split(isSubscription, wsLink, httpLink)

  // Оптимизация из доков Vue для SSR
  const cache = new InMemoryCache({
    fragmentMatcher,
    cacheRedirects
  })
  if (process.client) {
    if (typeof window !== 'undefined') {
      const state = window.__APOLLO_STATE__
      if (state) {
        cache.restore(state.defaultClient)
      }
    }
  }

  const middlewares = from([
    csrfMiddleware,
    ssrMiddleware,
    userStatusMiddleware,
    webSocketConnectionMiddleware
    // errorLink
  ])

  // Если тип операции subscription не используем middleware
  let link = split(
    isSubscription,
    concat(csrfMiddleware, httpLink),
    concat(middlewares, httpLink)
  )
  link = errorLink.concat(link)
  // Create the apollo client
  return {
    link,
    cache,
    typeDefs,
    resolvers,
    defaultHttpLink: false,
    // Set this on the server to optimize queries when SSR or temporary disable query force-fetching
    ...(process.server ? { ssrMode: true } : { ssrForceFetchDelay: 100 })
  }
}
