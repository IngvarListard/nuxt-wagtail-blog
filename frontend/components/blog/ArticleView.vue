<template>
  <div>
    <!-- Head image -->
    <v-card flat>
      <v-img
        :src="require('@/assets/Real-Python-Video-Tutorials_Watermarked.webp')"
        aspect-ratio="1.7"
      />
    </v-card>
    <div class="font-weight-bold mt-4" style="font-size: 36px">Cool New Features in Python 3.8</div>
    <div>
      <v-icon>mdi-account</v-icon>
      admin
      <v-icon class="ml-2">mdi-calendar</v-icon>
      Окт. 15, 2019
      <v-icon class="ml-2">mdi-comment-multiple-outline</v-icon>
      2
      <v-icon class="ml-2">mdi-tag-multiple</v-icon>
      <v-chip small label link style="color: gray;"><strong>Спорт</strong></v-chip>
      <v-chip small label link style="color: gray;"><strong>Отдых</strong></v-chip>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleView'
}
</script>

<style scoped>
.article-info {
  font-size: 14px;
  color: #999999;
}
</style>
