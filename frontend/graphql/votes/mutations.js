import gql from 'graphql-tag'

const VOTE_ARTICLE = gql`
  mutation($articleId: ID!, $action: String!) {
    vote(action: $action, articleId: $articleId) {
      success
    }
  }
`

export { VOTE_ARTICLE }
