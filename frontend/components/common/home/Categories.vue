<template>
  <v-card outlined>
    <v-card-title>Категории</v-card-title>
    <v-list>
      <v-list-item v-for="(btn, i) of buttons" :key="i">
        <v-list-item-action>
          <v-icon>mdi-folder</v-icon>
        </v-list-item-action>
        <v-list-item-content>{{ btn.name }}</v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Categories',
  computed: {
    ...mapState({
      buttons: state => state.layout.buttons
    })
  }
}
</script>

<style scoped>

</style>
