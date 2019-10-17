<template>
  <v-row justify="center">
    <v-col sm="12" lg="10">
      <v-row justify="center">
        <v-col
          v-for="article of articles"
          :key="article.id"
          lg="4"
          md="6"
          sm="12"
        >
          <div class="my-2">
            <v-card
              flat
              :to="{ name: 'article-slug', params: { slug: article.slug } }"
            >
              <v-img
                :src="
                  article.headImage
                    ? resolveUrl(article.headImage.rendition.url)
                    : require('@/assets/Real-Python-Video-Tutorials_Watermarked.webp')
                "
                aspect-ratio="1.8"
              />
            </v-card>
            <v-card-title
              style="color: #619CCD; font-size: 22px;"
              class="px-0 pt-2"
            >
              <n-link
                :to="{ name: 'article-slug', params: { slug: article.slug } }"
                ><span class="txt">{{ article.title }}</span></n-link
              >
            </v-card-title>
            <v-card-text class="px-0">
              <v-icon small>mdi-calendar</v-icon>
              Окт. 15, 2019
              <v-icon small class="mb-1">mdi-tag-multiple</v-icon>
              <v-chip x-small label link class="mb-1">Спорт</v-chip>
              <v-chip x-small label link class="mb-1">Отдых</v-chip>
            </v-card-text>
          </div>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import { GET_ARTICLES } from '../../../graphql/blog/queries'
import utilsMixin from '../../../utils/utilsMixin'

export default {
  name: 'Feed',
  mixins: [utilsMixin],
  apollo: {
    articles: {
      query: GET_ARTICLES
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
