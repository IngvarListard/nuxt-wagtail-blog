import { UPDATE_USER_INFO } from '../../../graphql/users/mutations'

export default {
  methods: {
    saveUser({
      id = null,
      firstName = null,
      lastName = null,
      bio = null,
      displayName = null,
      options = { loading: 0 }
    }) {
      options.loading += 1
      options.dialog = false
      return this.$apollo
        .mutate({
          mutation: UPDATE_USER_INFO,
          variables: {
            id,
            firstName,
            lastName,
            bio,
            displayName
          }
        })
        .then(() => {
          options.loading -= 1
        })
        .catch(e => {
          options.loading -= 1
          throw new Error(e)
        })
    }
  }
}
