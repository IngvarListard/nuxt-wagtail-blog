<template>
  <v-text-field
    ref="field"
    v-model="line"
    append-icon="mdi-magnify"
    placeholder="Искать на сайте"
    single-line
    hide-details
    clearable
    solo
    flat
    height="40"
    outlined
    @keyup.enter="search"
  />
</template>

<script>
export default {
  name: 'SearchField',
  data() {
    return {
      line: ''
    }
  },
  methods: {
    search() {
      this.$router.push({ name: 'search', query: { search: this.line } })
      this.line = ''
      this.$refs.field.blur()
    }
  }
}
</script>

<style scoped></style>
