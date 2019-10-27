<template>
  <v-navigation-drawer>
    <v-list shaped>
      <list-item></list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import ListItem from '../../components/common/ListItem'
export default {
  name: 'Profile',
  components: { ListItem },
  layout: 'profile'
}
</script>

<style scoped></style>
