<template>
  <v-app-bar
    color="#47555E"
    dark
    app
    :hide-on-scroll="$vuetify.breakpoint.xs"
    clipped-left
    flat
  >
    <v-app-bar-nav-icon class="hidden-md-and-up" @click="toggleDrawer" />
    <v-spacer />
    <n-link to="/">
      <v-img
        max-width="180px"
        :src="require('@/assets/logo/logo_transparent2.png')"
      />
    </n-link>
    <v-toolbar-items>
      <v-btn to="/" text nuxt class="ml-0 hidden-sm-and-down font-weight-light"
        >Публикации</v-btn
      >
      <v-btn
        to="/news"
        text
        nuxt
        class="ml-0 hidden-sm-and-down font-weight-light"
        >Новости</v-btn
      >
      <v-btn
        to="/events"
        text
        nuxt
        class="ml-0 hidden-sm-and-down font-weight-light"
        >События</v-btn
      >
      <search-field
        class="hidden-sm-and-down pt-3 pr-3"
        style="max-width: 420px"
      />
    </v-toolbar-items>
    <join-button v-if="!$$user.loggedIn" class="hidden-sm-and-down" />
    <v-spacer />
    <!--    <notifications v-if="$$user.loggedIn" class="hidden-sm-and-down" />-->
    <user-button v-if="$$user.loggedIn" class="hidden-sm-and-down" />
  </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
import Notifications from '../notifications/Notifications'
import DropDown from './DropDown'
import JoinButton from './JoinButton'
import SearchField from './SearchField'
import UserButton from './UserButton'

export default {
  name: 'AppBar',
  components: {
    Notifications,
    UserButton,
    SearchField,
    JoinButton,
    DropDown
  },
  computed: {
    ...mapState({
      buttons: state => state.layout.buttons
    })
  },
  methods: {
    ...mapMutations({
      toggleDrawer: 'layout/toggleDrawer'
    })
  }
}
</script>

<style>
.v-input__slot {
  min-height: 15px !important;
}
</style>
