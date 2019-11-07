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
import gql from 'graphql-tag'
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
