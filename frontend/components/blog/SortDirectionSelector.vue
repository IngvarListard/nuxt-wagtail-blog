<template>
  <v-select
    v-model="select"
    placeholder="Направление"
    :items="directions"
    outlined
    solo
    flat
    hide-details
  />
</template>

<script>
import _ from 'lodash'

export default {
  name: 'SortDirectionSelector',
  props: {
    value: {
      type: String,
      default: 'desc'
    }
  },
  data() {
    return {
      directions: [
        { text: 'По убыванию', value: 'desc' },
        { text: 'По возрастанию', value: 'asc' }
      ],
      select: this.value
    }
  },
  watch: {
    select(newVal) {
      const query = _.cloneDeep(this.$route.query)
      query.order = newVal
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
