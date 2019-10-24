<template>
  <div>e</div>
</template>

<script>
import { SOCIAL_AUTH } from '../../graphql/users/mutations'

export default {
  name: 'Callback',
  mounted() {
    const code = this.$route.hash
    const aaa = code.slice(1, code.length)
    console.log('AAAAAA', aaa)
    const params = new URLSearchParams(aaa)
    params.forEach((a, b) => { console.log( a, b )})
    this.$apollo
      .mutate({
        mutation: SOCIAL_AUTH,
        variables: {
          provider: 'vk-oauth2',
          accessToken: params.get('access_token')
        }
      })
      .then(data => {
        console.log(data)
      })
  }
}
</script>

<style scoped></style>
