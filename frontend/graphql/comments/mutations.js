import gql from 'graphql-tag'
import { COMMENT_FRAGMENT } from './queries'

const CREATE_COMMENT = gql`
  mutation($modelName: String!, $instanceId: ID!, $text: String!) {
    createComment(instanceId: $instanceId, modelName: $modelName, text: $text) {
      comment {
        ...CommentContents
      }
    }
  }
  ${COMMENT_FRAGMENT}
`

export { CREATE_COMMENT }
