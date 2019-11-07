import gql from 'graphql-tag'
import { NOTIFICATION_FRAGMENT } from './fragments'

const GET_PAGED_NOTIFICATIONS = gql`
  query($page: Int!, $perPage: Int!) {
    notificationsPage(page: $page, perPage: $perPage) {
      notifications {
        ...NotificationContents
      }
    }
  }
  ${NOTIFICATION_FRAGMENT}
`

export { GET_PAGED_NOTIFICATIONS }
