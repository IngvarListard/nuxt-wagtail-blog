import gql from 'graphql-tag'

const COMMENT_FRAGMENT = gql`
  fragment CommentContents on CommentNode {
    id
    objectId
    time
    user {
      id
      displayName
    }
    text
    parent {
      id
    }
    votesCount {
      id
      likes
      dislikes
      userVote
    }
    changed
    deleted
    childCount
  }
`
const GET_COMMENTS = gql`
  query($instanceId: ID!, $modelName: String!, $skip: Int!, $first: Int!) {
    comments(
      instanceId: $instanceId
      modelName: $modelName
      skip: $skip
      first: $first
    ) {
      id
      comments {
        ...CommentContents
      }
      totalCount
    }
  }
  ${COMMENT_FRAGMENT}
`
export { GET_COMMENTS, COMMENT_FRAGMENT }
