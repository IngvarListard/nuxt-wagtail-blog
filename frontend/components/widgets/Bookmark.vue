<template>
  <span>
    <v-btn icon>
      <v-icon>mdi-bookmark-outline</v-icon>
    </v-btn>
    {{ count }}
  </span>
</template>

<script>
export default {
  name: 'Bookmark',
  props: {
    count: {
      type: Number,
      required: true
    }
  }
}
</script>

<style scoped></style>
