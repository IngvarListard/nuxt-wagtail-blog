<template>
  <div>
    <v-card flat :to="{ name: 'article-slug', params: { slug: article.slug } }">
      <v-img :src="resolveArticleImage(article)" aspect-ratio="1.8" />
    </v-card>
    <v-card-title
      :style="{ color: '#619CCD', 'font-size': titleSize }"
      class="px-0 pt-2"
    >
      <slot name="title">
        <n-link :to="{ name: 'article-slug', params: { slug: article.slug } }"
          ><span class="txt">{{ article.title }}</span></n-link
        >
      </slot>
    </v-card-title>
    <v-card-text class="px-0">
      <slot name="text" />
      <v-icon small>mdi-calendar</v-icon>
      Окт. 15, 2019
      <v-icon small class="mb-1">mdi-tag-multiple</v-icon>
      <v-chip x-small label link class="mb-1">Спорт</v-chip>
      <v-chip x-small label link class="mb-1">Отдых</v-chip>
    </v-card-text>
  </div>
</template>

<script>
import utilsMixin from '../../utils/utilsMixin'

export default {
  name: 'ArticleCard',
  mixins: [utilsMixin],
  props: {
    article: {
      type: Object,
      default: () => ({})
    },
    titleSize: {
      type: String,
      default: '22px'
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
.txt {
  color: #619ccd;
  font-weight: normal;
}
a {
  text-decoration: none !important;
}
</style>
