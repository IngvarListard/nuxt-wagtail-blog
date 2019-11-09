<template>
  <span>
    <v-icon v-bind="options" class="mr-1">mdi-eye-outline</v-icon>
    <span
      class="font-weight-regular"
      style="font-size: 16px; color: #999999;"
      >{{ count }}</span
    >
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
      opts: {}
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
