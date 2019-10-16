<template>
  <v-app-bar color="#5F5F5F" dark fixed app flat hide-on-scroll>
    <v-app-bar-nav-icon class="hidden-md-and-up" @click="toggleDrawer" />
    <v-spacer />
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
          class="ml-0 hidden-sm-and-down"
          >{{ btn.name }}</v-btn
        >
      </template>
      <v-text-field
        append-icon="mdi-magnify"
        outlined
        placeholder="Искать на сайте"
        single-line
        hide-details
        clearable
        class="pt-1"
      />
    </v-toolbar-items>
    <v-spacer />
    <v-icon v-if="$$user.loggedIn" @click="logout">logout</v-icon>
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

<style scoped></style>
