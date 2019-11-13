<template>
  <v-navigation-drawer v-model="drawer" app temporary>
    <v-list dense>
      <!-- Поиск -->
      <v-list-item>
        <v-list-item-content class="py-1">
          <search-field />
        </v-list-item-content>
      </v-list-item>
      <v-divider />
      <v-subheader>НАВИГАЦИЯ</v-subheader>
      <list-item
        :btn="{ name: 'Публикации', icon: 'mdi-post-outline', route: '/' }"
      />
      <list-item
        :btn="{
          name: 'Новости',
          icon: 'mdi-newspaper-variant-multiple-outline',
          route: '/news/'
        }"
      />
      <list-item
        :btn="{
          name: 'События',
          icon: 'mdi-calendar-check-outline',
          route: '/events/'
        }"
      />
      <v-divider />
      <!--suppress CheckEmptyScriptTag -->
      <portal-target name="drawer" />
      <!-- Присоединиться -->
      <v-list-item v-if="!$$user.loggedIn">
        <v-list-item-content>
          <join-button />
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
import ListItem from './ListItem'
import JoinButton from './JoinButton'
import SearchField from './SearchField'

export default {
  name: 'Drawer',
  components: { SearchField, JoinButton, ListItem },
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
