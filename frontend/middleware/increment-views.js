import { INCREMENT_ARTICLE_VIEWS } from '../graphql/blog/mutations'

export default ({
  route: {
    params: { slug }
  },
  app: {
    apolloProvider: { defaultClient }
  }
}) => {
  defaultClient.mutate({
    mutation: INCREMENT_ARTICLE_VIEWS,
    variables: {
      slug
    }
  })
}
