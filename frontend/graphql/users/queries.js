import gql from 'graphql-tag'
import { USER_FRAGMENT } from './fragments'

const GET_CURRENT_USER = gql`
  {
    getCurrentUser {
      ...UserContents
    }
  }
  ${USER_FRAGMENT}
`

const CURRENT_USER_CLIENT = gql`
  {
    getCurrentUser @client {
      ...UserContents
    }
  }
  ${USER_FRAGMENT}
`
export { GET_CURRENT_USER, CURRENT_USER_CLIENT }
