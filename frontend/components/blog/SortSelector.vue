<template>
  <v-select
    v-model="select"
    placeholder="Сортировать по..."
    :items="sort"
    outlined
    solo
    flat
    hide-details
  />
</template>

<script>
import _ from 'lodash'

export default {
  name: 'SortSelector',
  props: {
    value: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      sort: [
        { text: 'По рейтингу', value: 'rating' },
        { text: 'По просмотрам', value: 'views' },
        { text: 'По дате', value: 'date' }
      ],
      select: this.value
    }
  },
  watch: {
    select(newVal) {
      const query = _.cloneDeep(this.$route.query)
      query.sortBy = newVal
      this.$router.push({ name: 'search', query })
      this.$emit('input', newVal)
    },
    value(newVal) {
      this.select = newVal
    }
  }
}
</script>

<style scoped></style>
