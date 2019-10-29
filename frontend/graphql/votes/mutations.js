import gql from 'graphql-tag'

const TO_VOTE = gql`
  mutation($instanceId: ID!, $action: String!, $voteTo: String!) {
    vote(action: $action, instanceId: $instanceId, voteTo: $voteTo) {
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
