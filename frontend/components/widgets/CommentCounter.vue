<template>
  <span>
    <v-icon>mdi-comment-outline</v-icon>
    {{ count }}
  </span>
</template>

<script>
export default {
  name: 'CommentCounter',
  props: {
    count: {
      type: Number,
      required: true
    }
  }
}
</script>

<style scoped></style>
