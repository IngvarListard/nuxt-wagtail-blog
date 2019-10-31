<template>
  <div>
    <article-view :article="article" />
    <comments-block model-name="blog.BlogPage" :instance-id="article.id" />
  </div>
</template>

<script>
import ArticleView from '../../components/blog/ArticleView'
import { GET_ARTICLE } from '../../graphql/blog/queries'
import CommentsBlock from '../../components/comments/CommentsBlock'

export default {
  name: 'ArticlePage',
  components: {
    CommentsBlock,
    ArticleView
  },
  scrollToTop: true,
  middleware: 'increment-views',
  data() {
    return {
      article: {}
    }
  },
  apollo: {
    article: {
      query: GET_ARTICLE,
      variables() {
        const slug = this.$route.params.slug
        return {
          slug
        }
      },
      update({ article }) {
        this.$store.commit('article/setCurrentArticle', article)
        return article
      }
    }
  }
}
</script>

<style scoped></style>
