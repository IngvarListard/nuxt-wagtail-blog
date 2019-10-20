<template>
  <v-container>
    <v-row justify="center">
      <v-col lg="7" md="12" sm="12">
        <article-view :article="article" />
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
import { GET_ARTICLE } from '../../graphql/blog/queries'

export default {
  name: 'ArticlePage',
  components: {
    NewsletterSubscribe,
    TagsCard,
    ArticleView
  },
  middleware: 'increment-views',
  apollo: {
    article: {
      query: GET_ARTICLE,
      variables() {
        const slug = this.$route.params.slug
        return {
          slug
        }
      }
    }
  }
}
</script>

<style scoped></style>
