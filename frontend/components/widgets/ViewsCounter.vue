<template>
  <span>
    <v-icon v-bind="opts" class="mr-1">mdi-eye-outline</v-icon>
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
      opts: {  }
    }
  },
  watch: {
    options(newVal) {
      // Object.assign(this.opts, newVal)
    }
  }
}
</script>

<style scoped></style>
