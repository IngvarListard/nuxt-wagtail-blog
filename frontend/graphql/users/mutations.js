import gql from 'graphql-tag'
import { USER_FRAGMENT } from './fragments'

const LOGIN = gql`
  mutation($login: String!, $password: String!) {
    login(login: $login, password: $password) {
      user {
        id
        isSuperuser
        firstName
        lastName
        email
        isActive
      }
      success
    }
  }
`

const LOGOUT = gql`
  mutation {
    logout {
      success
    }
  }
`

const SOCIAL_AUTH = gql`
  mutation SocialAuth($provider: String!, $accessToken: String!) {
    socialAuth(provider: $provider, accessToken: $accessToken) {
      social {
        uid
        extraData
      }
    }
  }
`

const UPDATE_AVATAR = gql`
  mutation($file: Upload!, $userId: ID!) {
    updateAvatar(file: $file, userId: $userId) {
      user {
        id
        avatar
      }
    }
  }
`

const UPDATE_USER_INFO = gql`
  mutation(
    $id: ID!
    $firstName: String
    $lastName: String
    $bio: String
    $displayName: String
  ) {
    updateUserInfo(
      id: $id
      firstName: $firstName
      lastName: $lastName
      displayName: $displayName
      bio: $bio
    ) {
      user {
        ...UserContents
      }
    }
  }
  ${USER_FRAGMENT}
`

const UPDATE_USER_EMAIL = gql`
  mutation($id: ID!, $email: String!) {
    updateUserEmail(id: $id, email: $email) {
      user {
        ...UserContents
      }
    }
  }
  ${USER_FRAGMENT}
`

const UPDATE_USER_PASSWORD = gql`
  mutation($id: ID!, $email: String!) {
    updateUserPassword(id: $id, password: $password) {
      success
    }
  }
`

export {
  LOGIN,
  LOGOUT,
  SOCIAL_AUTH,
  UPDATE_AVATAR,
  UPDATE_USER_INFO,
  UPDATE_USER_EMAIL,
  UPDATE_USER_PASSWORD
}
