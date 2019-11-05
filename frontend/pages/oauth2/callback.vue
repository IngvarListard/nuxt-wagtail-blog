<template>
  <div class="text-center">
    <v-progress-circular :size="300" :width="10" color="#47555E" indeterminate
      >Авторизация</v-progress-circular
    >
  </div>
</template>

<script>
import { SOCIAL_AUTH } from '../../graphql/users/mutations'

export default {
  name: 'Callback',
  mounted() {
    let hash = this.$route.hash
    this.$router.replace(this.$route.path)
    hash = hash.slice(1, hash.length)
    const params = new URLSearchParams(hash)
    const accessToken = params.get('access_token')
    const email = params.get('email')
    if (accessToken) {
      this.$apollo
        .mutate({
          mutation: SOCIAL_AUTH,
          variables: {
            provider: 'vk-oauth2',
            accessToken,
            email
          }
        })
        .then(data => {
          this.$router.replace('/')
        })
    } else {
      this.$router.replace('/')
    }
  }
}
</script>

<style scoped></style>
