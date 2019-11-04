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
                name: 'Темы',
                icon: 'mdi-message-settings-variant-outline',
                route: '/profile/settings/subscriptions/themes'
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
          console.log('DONE')
          return true
        }
      }
      return false
    }
  }
}
</script>

<style scoped></style>
