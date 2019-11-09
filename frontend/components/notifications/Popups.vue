<!-- eslint-disable vue/no-v-html -->
<template>
  <div style="bottom: 0; right: 0; position: fixed; z-index: 100">
    <v-scroll-x-reverse-transition group>
      <v-alert
        v-for="item in notificationsToShow"
        :key="item.id"
        v-model="item.show"
        border="left"
        dismissible
        class="slide-x-reverse-transition"
        width="500px"
        :type="typesMap[item.type]"
        prominent
      >
        <div v-html="item.text"></div>
        <template slot="close">
          <v-btn
            icon
            small
            nuxt
            :color="typesMap[item.type]"
            @click="hidePopup(item.id)"
          >
            <v-icon :color="typesMap[item.type]">close</v-icon>
          </v-btn>
        </template>
      </v-alert>
    </v-scroll-x-reverse-transition>
  </div>
</template>
<script>
import _ from 'lodash'
import { NOTIFICATIONS_STREAM } from '../../graphql/notifications/subscriptions'
import { GET_PAGED_NOTIFICATIONS } from '../../graphql/notifications/queries'

export default {
  name: 'Popups',
  data() {
    return {
      typesMap: {
        N: 'info',
        S: 'success',
        W: 'warning',
        C: 'error'
      },
      notificationsToShow: [],
      idCount: 1
    }
  },
  apollo: {
    notifications: {
      query: GET_PAGED_NOTIFICATIONS,
      variables() {
        return {
          page: 1,
          perPage: 10,
        }
      },
      skip() {
        return !this.$$user.loggedIn
      }
    },
    $subscribe: {
      // When a tag is added
      tagAdded: {
        query: NOTIFICATIONS_STREAM,
        result({
          data: {
            notifications: { notification }
          }
        }) {
          const newNotification = _.cloneDeep(notification)
          newNotification.id += this.idCount
          this.idCount++
          this.notificationsToShow.push(newNotification)
          setTimeout(() => {
            // this.notificationsToShow.splice(this.notificationsToShow.length - 1, this.notificationsToShow.length)
            this.notificationsToShow.splice(0, 1)
          }, 6000)
        }
      }
    }
  },
  // computed: {
  //   ...mapGetters('notifications', {
  //     notifications: 'nonDisplayedNotifications'
  //   })
  // },
  methods: {
    hidePopup(notificationId) {
      this.$store.commit('notifications/setDisplayStatus', {
        id: notificationId,
        show: false,
        displayed: false
      })
    }
  }
}
</script>
