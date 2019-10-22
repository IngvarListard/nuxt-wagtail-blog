import { toIdValue } from 'apollo-utilities'
import { defaultDataIdFromObject } from 'apollo-cache-inmemory';


const cacheRedirects = {
  Query: {
    article: (root, { id }) =>
      toIdValue(defaultDataIdFromObject({ __typename: 'ArticleNode', id }))
  }
}

export { cacheRedirects }
