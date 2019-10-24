<template>
  <v-container>
    <v-row justify="center">
      <v-col lg="11" md="12" sm="12" class="ma-0 pa-0">
        <v-row justify="center">
          <v-col cols="12" class="my-0 py-0">
            <v-row justify="center">
              <v-col
                v-for="article of articles"
                :key="article.id"
                cols="12"
                lg="4"
                md="6"
                sm="12"
                class="my-0 py-0"
              >
                <article-card :article="article" />
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
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
      query: GET_ARTICLES,
    }
  }
}
</script>

<style scoped>
</style>
