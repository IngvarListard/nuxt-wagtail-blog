import gql from 'graphql-tag'

export const USER_FRAGMENT = gql`
  fragment UserContents on BasicUserType {
    id
    isSuperuser
    firstName
    lastName
    email
    isActive
    displayName
    avatar
    bio
  }
`
