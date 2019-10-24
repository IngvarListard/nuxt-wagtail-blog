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

export { LOGIN, LOGOUT, SOCIAL_AUTH }
