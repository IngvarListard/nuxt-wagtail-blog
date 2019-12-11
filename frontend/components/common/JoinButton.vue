<template>
  <v-menu
    open-on-click
    bottom
    offset-y
    close-delay="300"
    transition="slide-y-transition"
  >
    <template #activator="{ on }">
      <v-btn
        color="red lighten-1"
        style="color: white;"
        elevation="0"
        depressed
        v-on="on"
        >Присоединиться</v-btn
      >
    </template>
    <v-list>
      <v-list-item>
        <a :href="link">
          <v-btn color="#4A739A">
            <span style="color: white;">Войти через</span>
            <v-icon class="px-2" large color="white">mdi-vk</v-icon>
          </v-btn>
        </a>
      </v-list-item>
<!--      <v-list-item>-->
<!--        <a :href="link">-->
<!--          <v-btn color="#3A5A9A">-->
<!--            <span style="color: white;">Войти через</span>-->
<!--            <v-icon class="px-2" large color="white">mdi-facebook</v-icon>-->
<!--          </v-btn>-->
<!--        </a>-->
<!--      </v-list-item>-->
<!--      <v-list-item>-->
<!--        <a :href="link">-->
<!--          <v-btn color="#EF5350">-->
<!--            <span style="color: white;">Войти через</span>-->
<!--            <v-icon class="px-2" large color="white">mdi-google-plus</v-icon>-->
<!--          </v-btn>-->
<!--        </a>-->
<!--      </v-list-item>-->
    </v-list>
  </v-menu>
</template>

<script>
export default {
  name: 'JoinButton',
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
  }
}
</script>

<style scoped>
a {
  text-decoration: none !important;
}
</style>
