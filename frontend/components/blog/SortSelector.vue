<template>
  <v-select
    placeholder="Сортировать по..."
    :items="sort"
    outlined
    solo
    flat
    hide-details
  />
</template>

<script>
export default {
  name: 'SortSelector',
  data() {
    return {
      sort: [
        { text: 'По рейтингу', value: 'rating' },
        { text: 'По просмотрам', value: 'viewed' }
      ]
    }
  }
}
</script>

<style scoped></style>
