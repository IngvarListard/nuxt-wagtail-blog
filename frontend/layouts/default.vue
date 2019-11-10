<template>
  <v-app style="background-color: white;">
    <alarms />
    <popups />
    <drawer />
    <app-bar />
    <v-content>
      <v-container>
        <v-row justify="center">
          <v-col lg="11" md="12" sm="12">
            <v-row justify="center">
              <v-col lg="8" md="12" sm="12">
                <nuxt />
              </v-col>
              <v-col lg="4" md="12" sm="12">
                <portal-target name="side">
                  <newsletter-subscribe />
                  <tags-card class="mt-4" />
                  <client-only>
                    <affix class="sidebar-menu" relative-element-selector="#example-content" style="width: 300px">
                      <a href="#markup-1">Markup 1</a>
                      <a href="#markup-2">Markup 2</a>
                      <a href="#markup-3">Markup 3</a>
                    </affix>
                    <section id="example-content">
                      <p>This is the #example-content section which the sidebar will be relatively affixed!</p>
                    </section>
                  </client-only>
                </portal-target>
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
import NewsletterSubscribe from '../components/common/home/NewsletterSubscribe'
import TagsCard from '../components/common/home/TagsCard'
import AppBar from '@/components/common/AppBar'
import Alarms from '@/components/common/Alarms'
import Drawer from '@/components/common/Drawer'
import Popups from '@/components/notifications/Popups'

export default {
  components: {
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
    this.$OneSignal.push(() => {
      this.$OneSignal.isPushNotificationsEnabled(isEnabled => {
        if (isEnabled) {
          console.log('Push notifications are enabled!')
        } else {
          console.log('Push notifications are not enabled yet.')
        }
      })
    })
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
