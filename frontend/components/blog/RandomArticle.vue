<template>
  <article-card :article="randomArticle" title-size="32px">
    <template #text>
      <div class="mb-2 text--primary" style="font-size: 17px; line-height: 1.5">
        {{ randomArticle.intro }}
      </div>
    </template>
  </article-card>
</template>

<script>
import { GET_RANDOM_ARTICLE } from '../../graphql/blog/queries'
import utilsMixin from '../../utils/utilsMixin'
import ArticleCard from './ArticleCard'

export default {
  name: 'RandomArticle',
  components: {
    ArticleCard
  },
  mixins: [utilsMixin],
  apollo: {
    randomArticle: {
      query: GET_RANDOM_ARTICLE
    }
  }
}
</script>

<style scoped>
.txt:hover {
  text-decoration: underline;
  cursor: pointer;
  color: #3676ab;
}
</style>
