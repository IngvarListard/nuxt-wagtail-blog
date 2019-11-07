<template>
  <v-container fluid>
    <v-row>
      <v-col v-if="!md_sm_xs" lg="4" />
      <v-col lg="8" md="12" xs="12">
        <v-row>
          <v-col lg="9" md="8" sm="8" cols="8">
            <v-text-field
              outlined
              v-model="searchLine"
              height="50px"
            />
          </v-col>

          <v-col lg="3" cols="4">
            <v-btn
              class="white--text"
              color="red"
              @click="searchArticles"
              height="50px"
              width="100%"
              :loading="loading"
            >
              Search >>
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <v-row>
      <v-col v-if="!md_sm_xs" lg="4" />
      <v-col lg="8" md="12" xs="12">
        <v-row>
          <v-col
            v-for="article of articles"
            :key="article.id"
            cols="6"
          >
            <article-card :article="article" />
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ARTICLE_SEARCH } from '../../graphql/blog/queries'
import ArticleCard from '../../components/blog/ArticleCard'

export default {
  name: 'search',
  components: { ArticleCard },
  data() {
    return {
      searchLine: '',
      articles: [],
      loading: false
    }
  },
  methods: {
    searchArticles() {
      this.loading = true
      this.$apollo.query({
        query: ARTICLE_SEARCH,
        variables: {
          searchLine: this.searchLine
        }
      }).then((data) => {
        this.loading = false
        this.articles = data.data.articleSearch
      })
    }
  },
  computed: {
    md_sm_xs() {
      return this.$vuetify.breakpoint.md || this.$vuetify.breakpoint.sm || this.$vuetify.breakpoint.xs
    }
  },
  mounted() {
    this.searchLine = this.$route.params.query || ''
    this.searchArticles()
  }
}
</script>

<style scoped>

</style>