<template>
  <v-row>
    <v-icon x-large class="mx-2">mdi-account-circle-outline</v-icon>
    <v-textarea
      v-model="text"
      placeholder="Новый комментарий"
      outlined
      class="pt-6 px-2"
      auto-grow
      rounded
      row-height="22"
      counter="3000"
      rows="2"
    >
      <template #append>
        <v-scroll-x-transition>
          <v-icon v-if="text.length > 0" color="primary" @click="">
            mdi-send
          </v-icon>
        </v-scroll-x-transition>
      </template>
    </v-textarea>
  </v-row>
</template>

<script>
export default {
  name: 'CommentInput',
  data() {
    return {
      text: ''
    }
  }
}
</script>

<style scoped></style>
