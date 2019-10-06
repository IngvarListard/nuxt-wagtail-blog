<template>
  <v-dialog v-model="dialog" max-width="1000px">
    <template v-slot:activator="{ on }">
      <v-btn icon v-on="on">
        <v-badge v-model="haveNotice" right overlap>
          <span slot="badge"> {{ totalNotice }}</span>
          <v-icon>mdi-bell-ring</v-icon>
        </v-badge>
      </v-btn>
    </template>

    <v-card>
      <v-card-title>
        <span class="title">
          Уведомления
        </span>
        <v-spacer />
        <a>
          <v-icon @click="closeDialog">
            mdi-close
          </v-icon>
        </a>
      </v-card-title>

      <v-card-actions>
        <v-checkbox
          v-model="onlyUnconfirmed"
          label="Только неподтвержденные"
          hide-details
        />
        <v-spacer />
        <v-btn
          color="primary"
          :loading="loadingConfirmation"
          @click="doConfirmAllNotifications()"
        >
          Отметить все как прочитаное
        </v-btn>
      </v-card-actions>

      <div>
        <template v-if="notifications.length">
          <div
            v-for="(notification, index) in notifications"
            :key="index"
            class="notice"
            :class="notification.type"
            @click="openNotification(notification)"
          >
            <div>
              <div class="title notice-header">
                От {{ notification.created.shortName }} ({{
                  formatDateTime(notification.date)
                }})
              </div>
              <!-- eslint-disable-next-line vue/no-v-html -->
              <div class="notice-message" v-html="notification.text"></div>
            </div>
            <div class="confirmation" @click.stop>
              <v-checkbox
                v-model="notification.confirmed"
                color="info"
                hide-details
                :class="{ unclickable: notification.confirmed }"
                @click="doConfirmNotification(notification)"
              />
            </div>
          </div>
        </template>

        <div v-if="notifications.length === 0 && !loading">
          <v-alert :value="true" type="info">
            Список пуст
          </v-alert>
        </div>
      </div>

      <v-card-actions style="bottom: 0px;">
        <v-btn
          block
          color="green"
          dark
          :loading="loading"
          @click="loadNotifications"
          >Загрузить более ранние уведомления</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
// import utilMixin from '../../../crm/vue/common/utils'
// import {
//   getUnconfirmedNoticeCount,
//   getPagedNotice,
//   confirmNotification,
//   confirmAllNotifications
// } from './query'

export default {
  name: 'Notifications',
  mixins: [],
  data() {
    return {
      dialog: false,
      loading: false,
      loadingConfirmation: false,
      totalNotice: 0,
      notifications: [],
      page: 1,
      onlyUnconfirmed: false
    }
  },
  // apollo: {
  //   query: {
  //     fetchPolicy: 'network-only',
  //     pollInterval: 10000,
  //     query: getUnconfirmedNoticeCount,
  //     update(data) {
  //       this.totalNotice = data.getUnconfirmedNoticeCount
  //     }
  //   }
  // },
  computed: {
    haveNotice() {
      return !!this.totalNotice
    }
  },
  watch: {
    onlyUnconfirmed: function(newVal) {
      this.notifications = []
      this.page = 1
      this.queryNotifications(this.page)
    },
    dialog: function(newVal) {
      if (newVal) {
        this.notifications = []
        this.queryNotifications(1)
      }
    }
  },
  beforeMount() {
    // setInterval(this.doQueryNotifications, 10000)
  },
  methods: {
    closeDialog() {
      this.dialog = false
    },
    openNotification(notification) {
      if (notification.link) {
        window.open(notification.link, '_blank')
      }
      this.doConfirmNotification(notification)
    },
    loadNotifications() {
      this.loading = true
      this.page += 1
      this.queryNotifications(this.page)
    },
    doQueryNotifications(page) {
      page = page || 1
      if (this.dialog) {
        this.queryNotifications(page)
      }
    },
    queryNotifications(page) {
      this.loading = true
      this.$apollo
        .query({
          fetchPolicy: 'no-cache',
          query: getPagedNotice,
          variables: {
            page: page,
            onlyUnconfirmed: this.onlyUnconfirmed
          }
        })
        .then(({ data }) => {
          this.notifications.push(...this.cloneDeep(data.getPagedNotice))
          this.notifications = this.notifications
            .reverse()
            .filter((item, pos) => {
              return this.notifications.map(x => x.id).indexOf(item.id) === pos
            })
          this.notifications.sort((a, b) => b.date.localeCompare(a.date))
          this.loading = false
        })
    },
    doConfirmNotification(notification) {
      this.$apollo
        .mutate({
          mutation: confirmNotification,
          variables: {
            input: {
              id: notification.id
            }
          }
        })
        .then(({ data }) => {
          notification.confirmed = true
          this.$apollo.queries.query.refetch()
        })
    },
    doConfirmAllNotifications() {
      this.loadingConfirmation = true
      this.$apollo
        .mutate({
          mutation: confirmAllNotifications,
          fetchPolicy: 'no-cache',
          variables: { input: {} }
        })
        .then(({ data }) => {
          this.notifications.forEach(item => {
            item.confirmed = true
          })
          this.$apollo.queries.query.refetch()
          this.loadingConfirmation = false
        })
    }
  }
}
</script>

<style scoped>
.white-text {
  color: white;
}

.S {
  color: white;
  background: green;
  border-left: 7px solid darkgreen;
  cursor: pointer;
}

.S:hover {
  border-left: 7px solid #003200;
}

.N {
  color: #3c3c3c;
  background: lightgrey;
  border-left: 7px solid grey;
  cursor: pointer;
}

.N:hover {
  border-left: 7px solid #4e4e4e;
}

.C {
  color: white;
  background: indianred;
  border-left: 7px solid red;
  cursor: pointer;
}

.C:hover {
  border-left: 7px solid #80000d;
}

.W {
  color: white;
  background: darkorange;
  border-left: 7px solid yellow;
  cursor: pointer;
}

.W:hover {
  border-left: 7px solid #cdcd00;
}

.new-notice {
  transition: 3s;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.notice {
  position: relative;
  margin: 5px 10px;
  padding: 15px 20px;
}

.notice-message {
  margin-top: 15px;
}

.confirmation {
  position: absolute;
  right: -5px;
  top: -15px;
}

.top-text {
  font-size: 15pt;
}

.unclickable {
  pointer-events: none;
}
</style>
