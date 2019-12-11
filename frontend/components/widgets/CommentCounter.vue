<template>
  <span
    class="font-weight-regular"
    style="font-size: 16px; color: #999999;"
  >
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
