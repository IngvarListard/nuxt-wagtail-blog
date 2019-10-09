<template>
  <v-menu open-on-hover offset-y>
    <template v-slot:activator="{ on }">
      <v-btn text class="ml-0 hidden-sm-and-down" nuxt v-on="on"
        >{{ value.name }}
        <v-icon>mdi-chevron-down</v-icon>
      </v-btn>
    </template>
    <v-list>
      <list-item
        v-for="(category, index) of value.categories"
        :key="index"
        :btn="category"
      />
    </v-list>
  </v-menu>
</template>

<script>
import ListItem from './ListItem'

export default {
  name: 'DropDown',
  components: {
    ListItem
  },
  props: {
    value: {
      type: Object,
      default: () => ({})
    }
  }
}
</script>

<style scoped></style>
