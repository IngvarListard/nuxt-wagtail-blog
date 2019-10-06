<template>
  <div>
    test
    {{ userId }}
  </div>
</template>
<script>
export default {
  validate({ params, query, store, error }) {
    error('tobi pizda', ['test'])
    return true
  },
  computed: {
    userId() {
      return this.$route.params.id
    }
  }
}
</script>
