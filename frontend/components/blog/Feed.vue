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
    <div v-intersect.quiet="onIntersect" class="text-center">
      <v-progress-circular v-if="loading > 0" size="60" indeterminate />
    </div>
  </v-container>
</template>

<script>
import { GET_ARTICLES } from '../../graphql/blog/queries'
import ArticleCard from './ArticleCard'
import { mapState, mapMutations } from 'vuex'

export default {
  name: 'Feed',
  components: {
    ArticleCard
  },
  data() {
    return {
      articles: [],
      loading: 0,
      test: 0
    }
  },
  apollo: {
    articles() {
      const skip = 0
      const first = 12
      return {
        query: GET_ARTICLES,
        variables: {
          skip,
          first
        },
        loadingKey: 'loading',
        fetchPolicy: 'cache-first'
      }
    }
  },
  computed: {
    ...mapState({
      skip: state => state.articles.skip,
      first: state => state.articles.skip
    })
  },
  methods: {
    ...mapMutations({
      increaseSkip: 'articles/increaseSkip'
    }),
    onIntersect(entries, observer, isIntersecting) {
      if (this.$apollo.queries.articles.loading || !isIntersecting) return
      this.increaseSkip(12)
      this.$apollo.queries.articles.fetchMore({
        variables: {
          skip: this.skip,
          first: this.first
        },
        updateQuery: (previousResult, { fetchMoreResult }) => {
          const newArticles = fetchMoreResult.articles
          // TODO: добавить hasMore в ответ запроса articles
          // const hasMore = fetchMoreResult.tagsPage.hasMore
          // this.showMoreEnabled = hasMore
          return {
            articles: [...previousResult.articles, ...newArticles]
          }
        }
      })
    }
  }
}
</script>

<style scoped></style>
