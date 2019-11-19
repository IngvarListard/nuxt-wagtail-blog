<template>
  <v-select
    placeholder="Направление"
    :items="directions"
    item-value="desc"
    outlined
    solo
    flat
    hide-details
  />
</template>

<script>
export default {
  name: 'SortDirectionSelector',
  data() {
    return {
      directions: [
        { text: 'По возрастанию', desc: true },
        { text: 'По убыванию', desc: false }
      ]
    }
  }
}
</script>

<style scoped></style>
