<template>
  <div>
    <v-card flat :to="{ name: 'article-slug', params: { slug: article.slug } }">
      <v-img :src="resolveArticleImage(article)" aspect-ratio="1.8" />
    </v-card>
    <v-card-title :style="{ 'font-size': titleSize }" class="px-0 pb-1 pt-2">
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
        <v-icon>mdi-calendar</v-icon>
        <span
          class="font-weight-regular"
          style="font-size: 16px; color: #999999;"
          >{{ formatDate(article.date) }}</span
        >
        <views-counter :count="article.views" class="mx-1" />
        <vote-counter
          :instance-id="article.id"
          :count="article.votesCount"
          model-name="blog.BlogPage"
          class="mr-2"
        />
        <span class="inline-block">
          <v-icon v-if="article.tags && article.tags.length > 0"
            >mdi-tag-multiple</v-icon
          >
          <tag
            v-for="tag of article.tags"
            :key="tag.id"
            :tag="tag"
            class="ml-1"
          />
        </span>
      </slot>
    </v-card-text>
  </div>
</template>

<script>
import utilsMixin from '../../utils/utilsMixin'
import Tag from '../widgets/Tag'
import ViewsCounter from '../widgets/ViewsCounter'
import VoteCounter from '../widgets/VoteCounter'

export default {
  name: 'ArticleCard',
  components: {
    Tag,
    ViewsCounter,
    VoteCounter
  },
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
  word-wrap: break-word;
}
.txt {
  color: #619ccd;
  font-weight: normal;
  word-break: keep-all;
}
a {
  text-decoration: none !important;
}
</style>
