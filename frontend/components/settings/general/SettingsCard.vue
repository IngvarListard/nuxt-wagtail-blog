<template>
  <v-card outlined :max-width="maxWidth" class="ma-auto pa-0">
    <v-card-title
      :class="title"
      style="font-size: 22px;"
    >
      <slot name="title" />
    </v-card-title>
    <v-card-subtitle class="mx-2">
      <slot name="subtitle" />
    </v-card-subtitle>
    <slot name="avatar" />
    <slot name="body" />
  </v-card>
</template>

<script>
export default {
  name: 'SettingsCard',
  props: {
    maxWidth: {
      type: [Number, String],
      default: 800
    },
    titleClass: {
      type: Array,
      default: () => ['my-2']
    }
  },
  computed: {
    title() {
      const baseClasses = ['text-left', 'font-weight-regular', 'mx-2']
      return baseClasses.concat(this.titleClass)
    }
  }
}
</script>

<style scoped></style>
