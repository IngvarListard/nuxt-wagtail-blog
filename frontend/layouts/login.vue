<template>
  <v-app>
    <alarms />
    <drawer />
    <app-bar />
    <notifications-drawer v-model="notificationDrawer" />
    <v-content>
      <v-container>
        <v-row justify="center">
          <v-col lg="11" md="12" sm="12">
            <v-row justify="center">
              <nuxt />
            </v-row>
          </v-col>
        </v-row>
        <portal-target name="bottom" />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import AppBar from '@/components/common/AppBar'
import Alarms from '@/components/common/Alarms'
import Drawer from '@/components/common/Drawer'
import NotificationsDrawer from '@/components/notifications/NotificationsDrawer'

export default {
  components: {
    Alarms,
    NotificationsDrawer,
    Drawer,
    AppBar
  },
  data() {
    return {
      drawer: false,
      notificationDrawer: false
    }
  }
}
</script>
