<template>
  <div>
    <v-row>
      <v-col
        v-for="aNews of news"
        :key="aNews.id"
        cols="12"
        lg="6"
        md="6"
        sm="12"
      >
        <news-card :news="aNews" />
      </v-col>
    </v-row>
    <div v-intersect.quiet="onIntersect" class="text-center">
      <v-progress-circular v-if="loading > 0" size="60" indeterminate />
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import { GET_NEWS_PAGE } from '../../graphql/news/qeuries'
import NewsCard from '../../components/news/NewsCard'

export default {
  name: 'News',
  components: { NewsCard },
  data() {
    return {
      news: [],
      loading: 0
    }
  },
  apollo: {
    news() {
      const page = 1
      const pageSize = 12
      return {
        query: GET_NEWS_PAGE,
        variables: { page, pageSize },
        loadingKey: 'loading',
        update({ newsPage }) {
          newsPage = JSON.parse(newsPage)
          this.setHasNext(Boolean(newsPage.next))
          return newsPage.results
        }
      }
    }
  },
  computed: {
    ...mapState({
      page: state => state.news.page,
      perPage: state => state.news.perPage,
      hasNext: state => state.news.hasNext
    })
  },
  methods: {
    ...mapMutations({
      setPage: 'news/setPage',
      setHasNext: 'news/setHasNext'
    }),
    onIntersect(entries, observer, isIntersecting) {
      if (this.$apollo.queries.news.loading || !isIntersecting || !this.hasNext)
        return
      this.setPage(this.page + 1)
      this.$apollo.queries.news.fetchMore({
        variables: {
          page: this.page,
          perPage: this.perPage
        },
        updateQuery: (previousResult, { fetchMoreResult }) => {
          const newsPage = JSON.parse(fetchMoreResult.newsPage)
          const newArticles = newsPage.results
          const hasNext = Boolean(newsPage.next)
          this.$store.commit('news/setHasNext', hasNext)
          this.news = this.news.concat(newArticles)
        }
      })
    }
  }
}
</script>

<style scoped></style>
