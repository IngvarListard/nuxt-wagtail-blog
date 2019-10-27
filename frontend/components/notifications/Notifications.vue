<template>
  <v-menu
    open-on-hover
    bottom
    offset-y
    close-delay="300"
    transition="slide-y-reverse-transition"
  >
    <template #activator="{ on }">
      <v-btn icon v-on="on">
        <v-icon large>mdi-bell-outline</v-icon>
      </v-btn>
    </template>
    <v-list>
      <list-item
        :btn="{
          name: 'Уведомления',
          icon: 'mdi-settings-outline',
          route: `/profile/settings/general`
        }"
      />
    </v-list>
  </v-menu>
</template>

<script>
import ListItem from '../common/ListItem'
export default {
  name: 'Notifications',
  components: { ListItem }
}
</script>

<style scoped></style>
