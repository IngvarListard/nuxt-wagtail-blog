<!-- eslint-disable vue/no-v-html -->
<template>
  <v-navigation-drawer
    v-model="drawer"
    app
    right
    absolute
    temporary
    width="500px"
  >
    <v-list>
      <v-list-item
        v-for="item in notifications"
        :key="item.id"
        nuxt
        :to="item.link"
        class="mx-0 my-1 px-0 py-0"
      >
        <v-alert
          :type="typesMap[item.type]"
          dense
          prominent
          class="my-0 mx-1"
          transition="fade-transition"
        >
          <!-- <div v-html="item.text"></div> -->
          <div class="title">Title</div>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime, aut!
          Aliquid harum magnam, numquam perspiciatis natus ipsam ad fugiat
          nostrum tenetur illum saepe odio possimus ullam? Sunt veritatis earum
          tempora.
        </v-alert>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
export default {
  name: 'NotificationsDrawer',
  props: {
    value: {
      type: Boolean,
      default: false
    }
  },
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
    drawer: {
      get() {
        return this.value
      },
      set(newVal) {
        this.$emit('input', newVal)
      }
    },
    notifications() {
      return this.$store.state.notifications.notifications
    }
  }
}
</script>
