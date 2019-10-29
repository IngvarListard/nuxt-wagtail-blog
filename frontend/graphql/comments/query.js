import gql from 'graphql-tag'

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
        changed
        deleted
        childCount
        votesCount {
          id
          likes
          dislikes
          userVote
        }
      }
      totalCount
    }
  }
`
export { GET_COMMENTS }
