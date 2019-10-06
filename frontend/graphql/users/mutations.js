import gql from 'graphql-tag'

const login = gql`
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

const logout = gql`
  mutation {
    logout {
      success
    }
  }
`

export { login, logout }
