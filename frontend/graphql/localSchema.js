import { toIdValue } from 'apollo-utilities'

// const dataIdFromObject = object => object.id
const dataIdFromObject = object => `${object.__typename}:${object.id}`

const cacheRedirects = {
  Query: {
    article: (root, { id }) =>
      toIdValue(dataIdFromObject({ __typename: 'ArticleNode', id }))
    // team: (root, { id }) =>
    //   toIdValue(dataIdFromObject({ __typename: 'Team', id }))
  }
}

export { cacheRedirects, dataIdFromObject }
