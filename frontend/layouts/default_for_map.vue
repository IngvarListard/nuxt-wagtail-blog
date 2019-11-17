<template>
  <v-app style="background-color: white;">
    <alarms />
    <popups />
    <drawer />
    <app-bar />
    <v-content>
      <v-container id="content">
        <v-row justify="center">
          <v-col lg="11" md="12" sm="12" xs="12" cols="12">
            <v-row justify="center">
              <v-col lg="8" md="12" sm="12" xs="12" cols="12">
                <nuxt id="example-content" />
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <portal-target name="bottom" />
      </v-container>
    </v-content>
    <v-footer color="indigo" app absolute>
      AAAAA
    </v-footer>
  </v-app>
</template>

<script>
import AppBar from '@/components/common/AppBar'
import Alarms from '@/components/common/Alarms'
import Drawer from '@/components/common/Drawer'
import Popups from '@/components/notifications/Popups'

export default {
  components: {
    Alarms,
    Popups,
    Drawer,
    AppBar
  },
  props: {
    source: {
      type: String,
      default: ''
    }
  },
  mounted() {
    // пуши, начало работы
    // this.$OneSignal.push(() => {
    //   this.$OneSignal.isPushNotificationsEnabled(isEnabled => {
    //     if (isEnabled) {
    //       console.log('Push notifications are enabled!')
    //     } else {
    //       console.log('Push notifications are not enabled yet.')
    //     }
    //   })
    // })
  },
  data: () => ({
    drawer: false
  }),
  methods: {
    logout() {
      this.$$auth.logout()
    }
  }
}
</script>
<style>
  .vue-affix {
    width: 300px
  }
</style>
