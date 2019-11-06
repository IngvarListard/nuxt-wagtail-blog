<template>
  <v-app style="background-color: white;">
    <alarms />
    <popups />
    <drawer />
    <app-bar />
    <notifications-drawer v-model="notificationDrawer" />
    <v-content>
      <v-container>
        <v-row justify="center">
          <v-col lg="11" md="12" sm="12">
            <v-row justify="center">
              <v-col lg="8" md="12" sm="12">
                <nuxt />
              </v-col>
              <v-col lg="4" md="12" sm="12">
                <newsletter-subscribe />
                <tags-card class="mt-4" />
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
import NotificationsDrawer from '@/components/notifications/NotificationsDrawer'

export default {
  components: {
    Alarms,
    Popups,
    NotificationsDrawer,
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
    drawer: false,
    notificationDrawer: false
  }),
  apollo: {
    $subscribe: {
      // When a tag is added
      tagAdded: {
        query: gql`
          subscription {
            notifications {
              notification {
                id
                purpose {
                  id
                }
                created {
                  id
                }
                date
                text
                confirmed
                type
              }
            }
          }
        `,
        result({ data }) {
          console.log(data)
        }
      }
    }
  },
  methods: {
    logout() {
      this.$$auth.logout()
    }
  }
}
</script>
