import gql from 'graphql-tag'

const NOTIFICATION_FRAGMENT = gql`
  fragment NotificationContents on NotificationNode {
    id
    purpose {
      id
    }
    created {
      id
    }
    date
    text
    confirmed
    type
  }
`

export { NOTIFICATION_FRAGMENT }
