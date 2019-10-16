<template>
  <div>
    <v-card flat>
      <v-img
        :src="require('@/assets/Real-Python-Video-Tutorials_Watermarked.webp')"
        aspect-ratio="1.7"
      />
    </v-card>
    <v-card-title
      style="font-size: 32px; color: #619CCD"
      class="px-0 font-weight-light txt"
    >
      Emacs: The Best Python Editor?
    </v-card-title>
    <v-card-text class="px-0">
      <div class="text--primary" style="font-size: 17px; line-height: 1.5">
        In this step-by-step course, you'll master the Python range() function,
        learn how its implementation differs in Python 3 vs 2, and see how you
        can use it to write faster and more Pythonic code.
      </div>
      <div class="mt-2">
        <v-icon small>mdi-calendar</v-icon>
        Окт. 15, 2019
        <v-icon small class="mb-1">mdi-star</v-icon>
        <v-icon small class="mb-1">mdi-tag-multiple</v-icon>
        <v-chip x-small label link>Спорт</v-chip>
        <v-chip x-small label link>Отдых</v-chip>
      </div>
    </v-card-text>
  </div>
</template>

<script>
export default {
  name: 'RandomArticle'
}
</script>

<style scoped>
.txt:hover {
  text-decoration: underline;
  cursor: pointer;
  color: #3676ab;
}
</style>
