<template>
  <v-list-item @click="">
    <v-list-item-action class="custom-list-action font-weight-bold"
      >ПАРОЛЬ</v-list-item-action
    >
    <v-list-item-content>********</v-list-item-content>
    <v-list-item-action>
      <v-btn icon>
        <v-icon>mdi-pencil</v-icon>
      </v-btn>
    </v-list-item-action>
  </v-list-item>
</template>

<script>
export default {
  name: 'PasswordField'
}
</script>

<style scoped></style>
