import gql from 'graphql-tag'

const TO_VOTE = gql`
  mutation($instanceId: ID!, $action: String!, $modelName: String!) {
    vote(action: $action, instanceId: $instanceId, modelName: $modelName) {
      votesCount {
        id
        likes
        dislikes
        userVote
      }
    }
  }
`

export { TO_VOTE }
