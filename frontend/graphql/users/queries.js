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
const getCurrentUser = gql`
  {
    getCurrentUser {
      id
      isSuperuser
      firstName
      lastName
      email
      isActive
    }
  }
`

export { allUsers, getCurrentUser }
