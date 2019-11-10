import gql from 'graphql-tag'

const INCREMENT_ARTICLE_VIEWS = gql`
  mutation($slug: String!) {
    incrementArticleViews(slug: $slug) {
      article {
        id
        views
      }
    }
  }
`

export { INCREMENT_ARTICLE_VIEWS }
