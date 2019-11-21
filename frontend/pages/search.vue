<template>
  <div>
    <v-card outlined>
      <v-card-text class="pb-0">
        <v-row justify="space-around" dense class="mb-2" no-gutters>
          <v-col cols="12">
            <v-text-field
              ref="searchField"
              v-model="searchLine"
              label="Начните вводить запрос..."
              outlined
              solo
              flat
              hide-details
              class="py-0 my-0"
            />
          </v-col>
          <v-expand-transition>
            <v-row v-if="advancedSearch" dense>
              <v-col cols="12" lg="4" md="4" sm="12">
                <tags-select ref="tagsSelect" v-model="tags" />
              </v-col>
              <v-col cols="7" lg="5" md="5" sm="7">
                <sort-selector v-model="sortBy" />
              </v-col>
              <v-col cols="5" lg="3" md="3" sm="5">
                <sort-direction-selector v-model="order" />
              </v-col>
            </v-row>
          </v-expand-transition>
        </v-row>
      </v-card-text>
      <v-row justify="center" dense no-gutters>
        <v-tooltip
          bottom
          open-delay="1000"
          close-delay="300"
          transition="slide-y-transition"
        >
          <template #activator="{ on }">
            <v-btn
              small
              text
              width="100%"
              v-on="on"
              @click="advancedSearch = !advancedSearch"
            >
              <v-icon>{{
                advancedSearch ? 'mdi-chevron-up' : 'mdi-chevron-down'
              }}</v-icon>
            </v-btn>
          </template>
          Расширенный поиск
        </v-tooltip>
      </v-row>
    </v-card>
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
import _ from 'lodash'
import { ARTICLE_SEARCH_PAGE } from '../graphql/blog/queries'
import ArticleCard from '../components/blog/ArticleCard'
import TagsSelect from '../components/blog/TagsSelect'
import SortSelector from '../components/blog/SortSelector'
import SortDirectionSelector from '../components/blog/SortDirectionSelector'

export default {
  name: 'Search',
  components: { SortDirectionSelector, SortSelector, TagsSelect, ArticleCard },
  data() {
    return {
      articles: [],
      loading: 0,
      advancedSearch: false,
      hasNext: false,
      page: 1,
      perPage: 9,
      searchLine_: this.$route.query.search || '',
      tags: this.$route.query.tags || [],
      sortBy: this.$route.query.sortBy || 'rating',
      order: this.$route.query.order || 'desc'
    }
  },
  apollo: {
    articles: {
      query: ARTICLE_SEARCH_PAGE,
      variables() {
        const page = 1
        const perPage = this.perPage
        const searchLine = this.searchLine
        const tags = this.tags.concat(this.$route.query.tags || [])
        const sortBy = this.sortBy
        const order = this.order
        return {
          page,
          perPage,
          searchLine,
          tags,
          sortBy,
          order
        }
      },
      debounce: 0,
      loadingKey: 'loading',
      fetchPolicy: 'cache-and-network',
      update({ articleSearch: { articles, hasNext } }) {
        this.hasNext = hasNext
        return articles
      }
    }
  },
  computed: {
    searchLine: {
      get() {
        return this.searchLine_
      },
      set: _.debounce(
        function(newVal) {
          this.searchLine_ = newVal
        },
        process.server ? 0 : 700
      )
    }
  },
  watch: {
    searchLine(newVal) {
      const query = _.cloneDeep(this.$route.query)
      query.search = newVal
      this.$router.push({ name: 'search', query })
    },
    '$route.query'(newVal) {
      if (newVal.tags && !this.advancedSearch) {
        this.advancedSearch = true
      }
    }
  },
  mounted() {
    this.$refs.searchField.focus()
    if (this.tags.length > 0) {
      setTimeout(() => {
        this.advancedSearch = true
      }, 700)
    }
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
          tags: this.tags,
          sortBy: this.sortBy,
          order: this.order
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
