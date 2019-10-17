<template>
  <v-app-bar color="#47555E" dark fixed app flat hide-on-scroll>
    <v-app-bar-nav-icon class="hidden-md-and-up" @click="toggleDrawer" />
    <v-spacer />
    <v-img max-width="180px" :src="require('@/assets/logo/logo_transparent2.png')" to="/" />
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
      <v-text-field
        append-icon="mdi-magnify"
        placeholder="Искать на сайте"
        single-line
        hide-details
        clearable
        solo
        flat
        height="40"
        outlined
        class="pt-3 pr-3"
        style="max-width: 220px"
      />
    </v-toolbar-items>
    <v-btn color="red lighten-1" elevation="0">Присоединиться</v-btn>
    <v-spacer />
    <v-icon v-if="$$user.loggedIn">logout</v-icon>
  </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
import DropDown from './DropDown'

export default {
  name: 'AppBar',
  components: {
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
