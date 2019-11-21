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
      this.$emit('input', newVal)
    }
  }
}
</script>

<style scoped></style>
