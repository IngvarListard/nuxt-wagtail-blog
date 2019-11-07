import gql from 'graphql-tag'
import { NOTIFICATION_FRAGMENT } from './fragments'

const NOTIFICATIONS_STREAM = gql`
  subscription {
    notifications {
      notification {
        ...NotificationContents
      }
    }
  }
  ${NOTIFICATION_FRAGMENT}
`

export { NOTIFICATIONS_STREAM }
