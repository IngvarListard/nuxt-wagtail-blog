<template>
  <v-row justify="center">
    <v-col sm="12" lg="10">
      <v-row justify="center">
        <v-col
          v-for="article of articles"
          :key="article.id"
          lg="4"
          md="6"
          sm="12"
        >
          <article-card :article="article" class="my-2" />
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import { GET_ARTICLES } from '../../graphql/blog/queries'
import ArticleCard from './ArticleCard'

export default {
  name: 'Feed',
  components: {
    ArticleCard
  },
  data() {
    return {
      articles: []
    }
  },
  apollo: {
    articles: {
      query: GET_ARTICLES
    }
  }
}
</script>

<style scoped>
</style>
