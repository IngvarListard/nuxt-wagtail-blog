<template>
  <v-navigation-drawer app clipped>
    <v-list shaped>
      <client-only>
        <portal to="drawer" :disabled="disablePortal">
          <v-subheader v-if="!disablePortal">УПРАВЛЕНИЕ ПРОФИЛЕМ</v-subheader>
          <list-item
            :btn="{
              name: 'Основные',
              icon: 'mdi-account-circle-outline',
              route: '/profile/settings/general'
            }"
          />

          <!--          <list-item-->
          <!--            :btn="{-->
          <!--              name: 'Закладки',-->
          <!--              icon: 'mdi-bookmark-multiple-outline',-->
          <!--              route: '/profile/settings/bookmarks'-->
          <!--            }"-->
          <!--          />-->
          <!--          <list-item-->
          <!--            :btn="{-->
          <!--              name: 'Уведомления',-->
          <!--              icon: 'mdi-bell-outline',-->
          <!--              route: '/profile/settings/notifications'-->
          <!--            }"-->
          <!--          />-->
          <!--          <v-divider />-->
          <!--          <list-item-->
          <!--            :btn="{-->
          <!--              name: 'Баг репорт',-->
          <!--              icon: 'mdi-message-alert-outline',-->
          <!--              route: '/feedback'-->
          <!--            }"-->
          <!--          />-->
        </portal>
      </client-only>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import ListItem from '../common/ListItem'
export default {
  name: 'SettingsDrawer',
  components: { ListItem },
  computed: {
    disablePortal() {
      const breakpoints = ['lg', 'md']
      for (let i = 0; i < breakpoints.length; i++) {
        if (this.$vuetify.breakpoint.name === breakpoints[i]) {
          return true
        }
      }
      return false
    }
  }
}
</script>

<style scoped></style>
