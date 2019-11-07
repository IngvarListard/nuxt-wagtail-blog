<template>
  <v-text-field
    append-icon="mdi-magnify"
    placeholder="Искать на сайте"
    v-model="line"
    single-line
    hide-details
    clearable
    solo
    flat
    height="40"
    outlined
    v-on:keyup.enter="search"
    ref="field"
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
      this.$router.push({ path: `/search/${this.line}` })
      this.line = ''
      this.$refs.field.blur()
    }
  }
}
</script>

<style scoped></style>
