<template>
  <article-view :article="article" />
</template>

<script>
import ArticleView from '../../components/blog/ArticleView'
import { GET_ARTICLE } from '../../graphql/blog/queries'

export default {
  name: 'ArticlePage',
  components: {
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
