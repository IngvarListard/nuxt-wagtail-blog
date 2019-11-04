import { UPDATE_USER_INFO } from '../../../graphql/users/mutations'

export default {
  methods: {
    saveUser({
      id = null,
      firstName = null,
      lastName = null,
      bio = null,
      displayName = null,
      dialog = false,
      loading = 0
    }) {
      loading += 1
      dialog = false
      this.$apollo
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
          loading -= 1
        })
        .catch(e => {
          loading -= 1
          throw new Error(e)
        })
    }
  }
}
