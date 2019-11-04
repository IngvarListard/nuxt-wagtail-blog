<template>
  <v-app style="background-color: white;">
    <alarms />
    <drawer />
    <app-bar />
    <settings-drawer />
    <v-content>
      <v-container>
        <nuxt />
        <portal-target name="bottom" />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import SettingsDrawer from '../components/settings/SettingsDrawer'
import AppBar from '@/components/common/AppBar'
import Alarms from '@/components/common/Alarms'
import Drawer from '@/components/common/Drawer'

export default {
  components: {
    SettingsDrawer,
    Alarms,
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
