<template>
  <div>
    <v-card flat :to="{ name: 'article-slug', params: { slug: article.slug } }">
      <v-img :src="resolveArticleImage(article)" aspect-ratio="1.8" />
    </v-card>
    <v-card-title :style="{ 'font-size': titleSize }" class="px-0 pt-2">
      <slot name="title">
        <n-link :to="{ name: 'article-slug', params: { slug: article.slug } }"
          ><span style="color: #619CCD;" class="txt">{{
            article.title
          }}</span></n-link
        >
      </slot>
    </v-card-title>
    <v-card-text class="px-0">
      <slot name="text" />
      <slot name="widgets">
        <v-icon v-bind="widgetSize.icons">mdi-calendar</v-icon>
        Окт. 15, 2019
        <v-icon v-bind="widgetSize.icons" class="mb-1">mdi-tag-multiple</v-icon>
        <v-chip v-bind="widgetSize.chips" label link class="mb-1">Спорт</v-chip>
        <v-chip v-bind="widgetSize.chips" label link class="mb-1">Отдых</v-chip>
      </slot>
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
    },
    widgetsSize: {
      // small, regular
      type: String,
      default: 'small'
    }
  },
  computed: {
    widgetSize() {

      const size = { chips: {}, icons: {} }
      switch (this.widgetsSize) {
        case 'small': {
          size.chips['x-small'] = true
          size.icons.small = true
          break
        }
        case 'regular': {
          size.chips.small = true
          break
        }
      }
      return size
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
