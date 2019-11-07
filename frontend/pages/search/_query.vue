<template>
  <div>
    <v-row justify="space-around" dense class="mb-2">
      <v-col cols="12" lg="8" md="8" sm="12">
        <v-text-field
          v-model="searchLine"
          label="Искать на сайте"
          outlined
          height="56px"
          hide-details
        />
      </v-col>
      <v-col cols="12" lg="3" md="3" sm="12">
        <v-btn
          class="white--text"
          color="red"
          height="56px"
          width="100%"
          :loading="loading"
          @click="searchArticles"
        >
          Search >>
        </v-btn>
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
  </div>
</template>

<script>
import { ARTICLE_SEARCH } from '../../graphql/blog/queries'
import ArticleCard from '../../components/blog/ArticleCard'

export default {
  name: 'Search',
  components: { ArticleCard },
  data() {
    return {
      searchLine: '',
      articles: [],
      loading: false
    }
  },
  computed: {
    md_sm_xs() {
      return (
        this.$vuetify.breakpoint.md ||
        this.$vuetify.breakpoint.sm ||
        this.$vuetify.breakpoint.xs
      )
    }
  },
  mounted() {
    this.searchLine = this.$route.params.query || ''
    this.searchArticles()
  },
  methods: {
    searchArticles() {
      this.loading = true
      this.$apollo
        .query({
          query: ARTICLE_SEARCH,
          variables: {
            searchLine: this.searchLine
          }
        })
        .then(data => {
          this.loading = false
          this.articles = data.data.articleSearch
        })
    }
  }
}
</script>

<style scoped></style>
