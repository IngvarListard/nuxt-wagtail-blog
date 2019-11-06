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
import { mapState, mapMutations } from 'vuex'
import { GET_PAGED_ARTICLES } from '../../graphql/blog/queries'
import ArticleCard from './ArticleCard'

export default {
  name: 'Feed',
  components: {
    ArticleCard
  },
  data() {
    return {
      articles: [],
      loading: 0
    }
  },
  apollo: {
    articles() {
      const page = 1
      const perPage = 12
      return {
        query: GET_PAGED_ARTICLES,
        variables: {
          page,
          perPage
        },
        loadingKey: 'loading',
        fetchPolicy: 'cache-first',
        update({ articlesPage }) {
          this.setHasNext = articlesPage.hasNext
          return articlesPage.articles
        }
      }
    }
  },
  computed: {
    ...mapState({
      page: state => state.articles.page,
      perPage: state => state.articles.perPage,
      hasNext: state => state.articles.hasNext
    })
  },
  methods: {
    ...mapMutations({
      setPage: 'articles/setPage',
      setHasNext: 'articles/setHasNext'
    }),
    onIntersect(entries, observer, isIntersecting) {
      if (
        this.$apollo.queries.articles.loading ||
        !isIntersecting ||
        !this.hasNext
      )
        return
      this.setPage(this.page + 1)
      this.$apollo.queries.articles.fetchMore({
        variables: {
          page: this.page,
          perPage: this.perPage
        },
        updateQuery: (previousResult, { fetchMoreResult }) => {
          const newArticles = fetchMoreResult.articlesPage.articles
          const hasNext = fetchMoreResult.articlesPage.hasNext
          this.$store.commit('articles/setHasNext', hasNext)
          return {
            articlesPage: {
              __typename: previousResult.articlesPage.__typename,
              hasNext,
              articles: [
                ...previousResult.articlesPage.articles,
                ...newArticles
              ]
            }
          }
        }
      })
    }
  }
}
</script>

<style scoped></style>
