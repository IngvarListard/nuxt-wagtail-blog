<template>
  <v-navigation-drawer
    class="hidden-sm-and-down"
    absolute
    clipped
    disable-resize-watcher
    permanent
  >
    <v-list shaped>
      <list-item
        :btn="{
          name: 'Основные',
          icon: 'mdi-account-circle-outline',
          route: '/profile/settings/general'
        }"
      />

      <v-list-group no-action>
        <list-item
          slot="activator"
          :btn="{
            name: 'Подписки',
            icon: 'mdi-playlist-check'
          }"
          class="mx-0 px-0"
          no-action
        />
        <list-item
          :btn="{
            name: 'Авторы',
            icon: 'mdi-account-group-outline',
            route: '/profile/settings/subscriptions/users'
          }"
        />
        <list-item
          :btn="{
            name: 'Компании',
            icon: 'mdi-bank-outline',
            route: '/profile/settings/subscriptions/companies'
          }"
        />
        <list-item
          :btn="{
            name: 'Своя',
            icon: 'mdi-message-settings-variant-outline',
            route: '/profile/settings/subscriptions/custom'
          }"
        />
      </v-list-group>
      <list-item
        :btn="{
          name: 'Закладки',
          icon: 'mdi-bookmark-multiple-outline',
          route: '/profile/settings/bookmarks'
        }"
      />
      <list-item
        :btn="{
          name: 'Активность',
          icon: 'mdi-star-circle-outline',
          route: '/profile/settings/activity'
        }"
      />
      <list-item
        :btn="{
          name: 'Уведомления',
          icon: 'mdi-bell-outline',
          route: '/profile/settings/notifications'
        }"
      />
      <v-divider />
      <list-item
        :btn="{
          name: 'Отправить отзыв',
          icon: 'mdi-message-alert-outline',
          route: '/feedback'
        }"
      />
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import ListItem from '../common/ListItem'
export default {
  name: 'SettingsDrawer',
  components: { ListItem }
}
</script>

<style scoped></style>
