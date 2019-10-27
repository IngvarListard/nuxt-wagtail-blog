<template>
  <v-app-bar color="#47555E" dark fixed app flat hide-on-scroll>
    <v-app-bar-nav-icon class="hidden-md-and-up" @click="toggleDrawer" />
    <v-spacer />
    <n-link to="/">
      <v-img
        max-width="180px"
        :src="require('@/assets/logo/logo_transparent2.png')"
      />
    </n-link>
    <v-toolbar-items>
      <template v-for="(btn, i) of buttons">
        <drop-down
          v-if="btn.categories && btn.categories.length > 0"
          :key="i"
          :value="btn"
        />
        <v-btn
          v-else
          :key="i"
          :to="btn.route"
          text
          nuxt
          class="ml-0 hidden-sm-and-down font-weight-light"
          >{{ btn.name }}</v-btn
        >
      </template>
      <search-field
        class="hidden-sm-and-down pt-3 pr-3"
        style="max-width: 220px"
      />
    </v-toolbar-items>
    <join-button v-if="!$$user.loggedIn" class="hidden-sm-and-down" />
    <v-spacer />
    <notifications v-if="$$user.loggedIn" class="hidden-sm-and-down" />
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
