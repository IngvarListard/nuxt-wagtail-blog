<template>
  <v-app id="inspire">
    <alarms />
    <popups />
    <drawer />
    <app-bar />
    <notifications-drawer v-model="notificationDrawer" />
    <v-content>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer color="indigo" app>
      <span class="white--text">&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>
import AppBar from '@/components/common/AppBar'
import Alarms from '@/components/common/Alarms'
import Drawer from '@/components/common/Drawer'
import Popups from '@/components/notifications/Popups'
import NotificationsDrawer from '@/components/notifications/NotificationsDrawer'

export default {
  components: { Alarms, Popups, NotificationsDrawer, Drawer, AppBar },
  props: {
    source: {
      type: String,
      default: ''
    }
  },
  data: () => ({
    drawer: false,
    notificationDrawer: false
  }),
  methods: {
    logout() {
      this.$$auth.logout()
    },
  }
}
</script>
