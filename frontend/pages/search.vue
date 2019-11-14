<template>
  <div>
    <v-row justify="space-around" dense class="mb-2">
      <v-col cols="12" lg="7" md="7" sm="12">
        <v-text-field
          ref="searchField"
          v-model="searchLine"
          label="Начните вводить запрос..."
          outlined
          solo
          flat
          hide-details
        />
      </v-col>
      <v-col cols="12" lg="5" md="5" sm="12">
        <tags-select />
      </v-col>
    </v-row>
    <v-row>
      <v-col
        v-for="article of articles"
        :key="article.id"
        cols="12"
        lg="6"
        md="6"
        sm="12"
      >
        <article-card :article="article" />
      </v-col>
    </v-row>
    <div v-intersect.quiet="onIntersect" class="text-center">
      <v-progress-circular v-if="loading > 0" size="60" indeterminate />
    </div>
  </div>
</template>

<script>
import { ARTICLE_SEARCH_PAGE } from '../graphql/blog/queries'
import ArticleCard from '../components/blog/ArticleCard'
import TagsSelect from '../components/blog/TagsSelect'

export default {
  name: 'Search',
  components: { TagsSelect, ArticleCard },
  data() {
    return {
      searchLine: '',
      articles: [],
      loading: 0,
      tags: [],
      hasNext: true,
      page: 1,
      perPage: 9
    }
  },
  apollo: {
    articles: {
      query: ARTICLE_SEARCH_PAGE,
      variables() {
        const page = 1
        const perPage = this.perPage
        const searchLine = this.searchLine
        const tags = this.$route.query.tags
        return {
          page,
          perPage,
          searchLine,
          tags
        }
      },
      debounce: 500,
      loadingKey: 'loading',
      update({ articleSearch: { articles, hasNext } }) {
        this.hasNext = hasNext
        return articles
      },
      skip() {
        return this.searchLine.length === 0 && this.tags.length === 0
      }
    }
  },
  watch: {
    searchLine(newVal) {
      this.$router.push({ name: 'search', query: { search: newVal } })
    }
  },
  mounted() {
    this.$refs.searchField.focus()
    this.searchLine = this.$route.query.search || ''
    this.tags = this.$route.query.tags || []
  },
  methods: {
    onIntersect(entries, observer, isIntersecting) {
      if (
        this.$apollo.queries.articles.loading ||
        !isIntersecting ||
        !this.hasNext
      )
        return
      this.page++
      this.$apollo.queries.articles.fetchMore({
        variables: {
          page: this.page,
          perPage: this.perPage,
          searchLine: this.searchLine,
          tags: this.tags
        },
        updateQuery: (previousResult, { fetchMoreResult }) => {
          const newArticles = fetchMoreResult.articleSearch.articles
          const hasNext = fetchMoreResult.articleSearch.hasNext
          this.hasNext = hasNext
          return {
            articleSearch: {
              __typename: previousResult.articleSearch.__typename,
              hasNext,
              articles: [
                ...previousResult.articleSearch.articles,
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
