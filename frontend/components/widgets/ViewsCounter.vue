<template>
  <span>
    <v-icon v-bind="options" class="mr-1">mdi-eye-outline</v-icon>
    <span>{{ count }}</span>
  </span>
</template>

<script>
export default {
  name: 'ViewsCounter',
  props: {
    count: {
      type: Number,
      default: 0
    },
    options: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      opts: { small: true }
    }
  },
  watch: {
    options(newVal) {
      this.opts = Object.assign(newVal, this.opts)
    }
  }
}
</script>

<style scoped></style>
