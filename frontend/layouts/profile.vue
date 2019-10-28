<template>
  <v-app>
    <alarms />
    <drawer />
    <app-bar />
    <settings-drawer />
    <v-content>
      <v-card height="100%">
        <v-container>
          <nuxt />
          <portal-target name="bottom" />
        </v-container>
      </v-card>
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
