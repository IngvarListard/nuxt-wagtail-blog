<template>
  <v-container fluid fill-height>
    <v-row justify="center" align="center">
      <a :href="link">
        <v-btn x-large color="primary">
          Войти через вконтакте
        </v-btn>
      </a>
    </v-row>
  </v-container>
</template>

<script>
export default {
  // layout: 'login',
  computed: {
    link() {
      return (
        'https://oauth.vk.com/authorize?' +
        'client_id=7178463&' +
        'display=page&' +
        'redirect_uri=http://localhost:3000/oauth2/callback&' +
        'response_type=token&' +
        'scope=email'
      )
    }
  }
}
</script>

<style scoped></style>
