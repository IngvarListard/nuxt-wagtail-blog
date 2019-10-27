<template>
  <v-container fluid fill-height>
    <v-row justify="center" align="center">
      <client-only>
        <a :href="link">
          <v-btn x-large color="primary">
            Войти через вконтакте
          </v-btn>
        </a>
      </client-only>
    </v-row>
  </v-container>
</template>

<script>
export default {
  layout: 'one-col',
  computed: {
    link() {
      const route = !this.$isServer ? window.location.origin : ''
      return (
        'https://oauth.vk.com/authorize?' +
        `client_id=${process.env.VK_CLIENT_ID}&` +
        'display=page&' +
        `redirect_uri=${route}/oauth2/callback&` +
        'response_type=token&' +
        'scope=email'
      )
    }
  },
  middleware(ctx) {
    if (ctx.store.state.auth.user.loggedIn) {
      ctx.redirect('/')
    }
  }
}
</script>

<style scoped></style>
