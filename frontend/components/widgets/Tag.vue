<template>
  <v-chip
    v-bind="opts"
    color="#F6F6F6"
    :to="{ name: 'tag-slug', params: { slug: tag.slug } }"
    class="my-1"
    small
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
      default: () => ({ label: true })
    },
    tag: {
      type: Object,
      default: () => ({ name: '', slug: '' })
    }
  },
  data() {
    return {
      opts: { label: true }
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
