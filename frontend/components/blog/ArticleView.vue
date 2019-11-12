<template>
  <div>
    <!-- Head image -->
    <article-card :article="article" title-size="34px" widgets-size="regular">
      <template #title>
        <span
          class="font-weight-bold"
          style="line-height: 1.25; word-break: keep-all;"
          >{{ article.title }}</span
        >
      </template>
    </article-card>
    <client-only>
      <toc-card
        v-if="Object.keys(article).length > 0"
        depth="3"
        font-size="16"
        class="mt-2"
        style="background-color: #F6F6F6;"
      />
    </client-only>
    <div v-for="(item, index) of article.body" :key="index">
      <!-- Заголовок первого уровня -->
      <template v-if="item.blockType === 'heading'">
        <h1>{{ item.value }}</h1>
      </template>
      <!-- Параграф -->
      <template v-else-if="item.blockType === 'paragraph'">
        <span v-html="item.value"></span>
      </template>
      <!-- Изображение -->
      <template v-else-if="item.blockType === 'image'">
        <v-card flat outlined>
          <v-img
            :src="resolveUrl(item.image.rendition.url)"
            aspect-ratio="1.8"
          />
        </v-card>
        <div style="text-align: center;" class="mb-4">
          <!--          <span class="text-truncate">{{ item.image.title }}</span>-->
        </div>
      </template>
      <template v-else-if="item.blockType === 'markdown'">
        <vue-markdown>{{ item.value }}</vue-markdown>
      </template>
      <!-- Блок кода -->
      <template v-else-if="item.blockType === 'code'">
        <client-only>
          <code-block
            class="line-numbers pb-4"
            :code="item.value.code"
            :language="item.value.language"
          />
        </client-only>
      </template>
    </div>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'
import utilsMixin from '../../utils/utilsMixin'
import ArticleCard from './ArticleCard'
import CodeBlock from './blocks/CodeBlock'
import TocCard from './TocCard'

export default {
  name: 'ArticleView',
  components: {
    TocCard,
    ArticleCard,
    VueMarkdown,
    CodeBlock
  },
  mixins: [utilsMixin],
  props: {
    article: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      blockTypes: ['heading', 'code', 'paragraph', 'image', 'markdown']
    }
  }
}
</script>

<style scoped>
.article-info {
  font-size: 14px;
  color: #999999;
}
</style>
