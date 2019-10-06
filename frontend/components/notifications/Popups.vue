<!-- eslint-disable vue/no-v-html -->
<template>
  <div style="bottom: 0; right: 0px; position: fixed; z-index: 100">
    <v-alert
      v-for="item in notifications"
      :key="item.id"
      v-model="item.show"
      colored-border
      border="left"
      dismissible
      transition="slide-x-reverse-transition"
      width="500px"
      :type="typesMap[item.type]"
      dense
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
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Popups',
  data() {
    return {
      typesMap: {
        N: 'info',
        S: 'success',
        W: 'warning',
        C: 'error'
      }
    }
  },
  computed: {
    ...mapGetters('notifications', {
      notifications: 'nonDisplayedNotifications'
    })
  },
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
