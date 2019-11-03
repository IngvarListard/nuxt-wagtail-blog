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
        <v-icon large>mdi-account-circle-outline</v-icon>
      </v-btn>
    </template>
    <v-list>
      <list-item
        :btn="{
          name: 'Управление профилем',
          icon: 'mdi-settings-outline',
          route: `/profile/settings/general`
        }"
      />
      <list-item
        :btn="{
          name: 'Подписки',
          icon: 'mdi-playlist-check',
          route: '/subscriptions'
        }"
      />
      <list-item
        :btn="{
          name: 'Закладки',
          icon: 'mdi-bookmark-multiple-outline',
          route: '/bookmarks-outline'
        }"
      />
      <list-item
        :btn="{
          name: 'Выход',
          icon: 'logout',
          route: '/logout'
        }"
      />
      <list-item
        :btn="{
          icon: 'mdi-theme-light-dark'
        }"
      >
        <template #content>
          <v-switch exact />
        </template>
      </list-item>
    </v-list>
  </v-menu>
</template>

<script>
import ListItem from './ListItem'
export default {
  name: 'UserButton',
  components: { ListItem }
}
</script>

<style scoped></style>
