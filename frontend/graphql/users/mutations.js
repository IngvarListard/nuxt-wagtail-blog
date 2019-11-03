import gql from 'graphql-tag'

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

export { LOGIN, LOGOUT, SOCIAL_AUTH, UPDATE_AVATAR }
