<template>
  <v-navigation-drawer v-model="drawer" app temporary>
    <v-list dense>
      <template v-for="(btn, i) of buttons">
        <v-list-group
          v-if="btn.categories && btn.categories.length > 0"
          :key="i"
          no-action
        >
          <list-item slot="activator" :btn="btn" class="mx-0 px-0" no-action />
          <list-item v-for="(category, index) of btn.categories" :key="index" :btn="category" />
        </v-list-group>
        <list-item v-else :key="i" :btn="btn" />
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
import ListItem from './ListItem'

export default {
  name: 'Drawer',
  components: { ListItem },
  computed: {
    ...mapState({
      buttons: state => state.layout.buttons
    }),
    drawer: {
      get() {
        return this.$store.state.layout.drawer
      },
      set(newVal) {
        this.$store.commit('layout/setDrawer', newVal)
      }
    }
  },
  methods: {
    ...mapMutations({
      toggleDrawer: 'layout/toggleDrawer'
    })
  }
}
</script>

<style scoped></style>
