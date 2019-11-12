<template>
  <div>
    <article-view id="article" :article="article" />
    <client-only>
      <v-row dense>
        <article-actions-block
          :instance-id="article.id"
          :comments-count="1"
          :views-count="article.views"
          :votes-count="article.votesCount"
          :bookmark-count="31"
          class="my-4"
        />
      </v-row>
      <author-card :author="article.owner" />
    </client-only>
    <support-author class="my-3" />
    <share-card />
    <comments-block model-name="blog.BlogPage" :instance-id="article.id" />
    <portal to="side-bottom">
      <client-only>
        <affix
          relative-element-selector="#example-content"
          style="width: 300px"
          :offset="{ top: -400, bottom: 0 }"
          class="hidden-md-and-down"
        >
          <toc-card
            v-if="loading === 0 && Object.keys(article).length > 0"
            depth="2"
            class="mt-4"
            font-size="14"
          />
        </affix>
      </client-only>
    </portal>
  </div>
</template>

<script>
import ArticleView from '../../components/blog/ArticleView'
import { GET_ARTICLE } from '../../graphql/blog/queries'
import CommentsBlock from '../../components/comments/CommentsBlock'
import ArticleActionsBlock from '../../components/blog/ArticleActionsBlock'
import AuthorCard from '../../components/widgets/AuthorCard'
import SupportAuthor from '../../components/blog/SupportAuthor'
import ShareCard from '../../components/blog/ShareCard'
import TableOfContent from '../../components/blog/TableOfContent.js'
import TocCard from "../../components/blog/TocCard";

export default {
  name: 'ArticlePage',
  middleware: 'increment-views',
  components: {
    TocCard,
    TableOfContent,
    ShareCard,
    SupportAuthor,
    AuthorCard,
    ArticleActionsBlock,
    CommentsBlock,
    ArticleView
  },
  scrollToTop: true,
  data() {
    return {
      article: {},
      loading: 0
    }
  },
  apollo: {
    article: {
      query: GET_ARTICLE,
      variables() {
        const slug = this.$route.params.slug
        return {
          slug
        }
      },
      loadingKey: 'loading'
    }
  }
}
</script>

<style scoped>
/*[id]::before {*/
/*  content: '';*/
/*  display: block;*/
/*  height: 75px;*/
/*  margin-top: -75px;*/
/*  visibility: hidden;*/
/*}*/
</style>
