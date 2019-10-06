<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <login-box />
    </v-layout>
  </v-container>
</template>

<script>
import LoginBox from '~/components/users/LoginBox'

export default {
  layout: 'login',
  components: {
    LoginBox
  }
}
</script>

<style scoped></style>
