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
              <v-col lg="4" md="12" sm="12" xs="12" cols="12">
                <portal-target name="side">
                  <newsletter-subscribe />
                  <tags-card class="mt-4" />
                </portal-target>
                <portal-target name="side-bottom" />
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <portal-target name="bottom" />
      </v-container>
    </v-content>
    <Footer />
  </v-app>
</template>

<script>
import NewsletterSubscribe from '../components/common/home/NewsletterSubscribe'
import TagsCard from '../components/common/home/TagsCard'
import Footer from '../components/common/Footer'
import AppBar from '@/components/common/AppBar'
import Alarms from '@/components/common/Alarms'
import Drawer from '@/components/common/Drawer'
import Popups from '@/components/notifications/Popups'

export default {
  components: {
    Footer,
    Alarms,
    Popups,
    Drawer,
    AppBar,
    NewsletterSubscribe,
    TagsCard
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
  width: 300px;
}
</style>
