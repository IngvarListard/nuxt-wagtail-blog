<template>
  <v-chip
    v-bind="opts"
    color="#d6d6d6"
    :to="{ name: 'tag-slug', params: { slug: tag.slug } }"
  >
    <strong style="color: gray">{{ tag.name }}</strong>
  </v-chip>
</template>

<script>
export default {
  name: 'Tag',
  props: {
    // опции v-chip
    options: {
      type: Object,
      default: () => ({ 'x-small': true, label: true })
    },
    tag: {
      type: Object,
      default: () => ({ name: '', slug: '' })
    }
  },
  data() {
    return {
      opts: { 'x-small': true, label: true }
    }
  },
  watch: {
    options(newVal) {
      Object.assign(this.opts, newVal)
    }
  }
}
</script>

<style scoped></style>
