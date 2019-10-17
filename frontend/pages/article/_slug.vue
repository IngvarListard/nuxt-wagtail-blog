<template>
  <v-container>
    <v-row justify="center">
      <v-col lg="7" md="12" sm="12">
        <article-view />
      </v-col>
      <v-col lg="3" md="12" sm="12">
        <newsletter-subscribe />
        <tags-card class="my-4" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NewsletterSubscribe from '../../components/common/home/NewsletterSubscribe'
import TagsCard from '../../components/common/home/TagsCard'
import ArticleView from '../../components/blog/ArticleView'

export default {
  name: 'ArticlePage',
  components: {
    NewsletterSubscribe,
    TagsCard,
    ArticleView
  }
}
</script>

<style scoped></style>
