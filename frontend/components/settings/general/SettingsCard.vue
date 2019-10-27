<template>
  <v-card outlined :max-width="maxWidth" class="ma-auto pa-0">
    <v-card-title
      class="text-left font-weight-regular my-2 mx-2"
      style="font-size: 22px;"
    >
      <slot name="title" />
    </v-card-title>
    <v-card-subtitle class="mx-2">
      <slot name="subtitle" />
    </v-card-subtitle>
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
    }
  }
}
</script>

<style scoped></style>
