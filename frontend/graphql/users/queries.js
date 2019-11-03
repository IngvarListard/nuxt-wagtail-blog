import gql from 'graphql-tag'

const allUsers = gql`
  {
    allUsers {
      id
      firstName
      lastName
    }
  }
`

const USER_FRAGMENT = gql`
  fragment UserContents on UserType {
    id
    isSuperuser
    firstName
    lastName
    email
    avatar
    isActive
  }
`

const GET_CURRENT_USER = gql`
  {
    getCurrentUser {
      id
      isSuperuser
      firstName
      lastName
      email
      avatar
      isActive
    }
  }
`

const CURRENT_USER_CLIENT = gql`
  {
    getCurrentUser @client {
      id
      isSuperuser
      firstName
      lastName
      email
      avatar
      isActive
    }
  }
`
export { GET_CURRENT_USER, CURRENT_USER_CLIENT, allUsers }
