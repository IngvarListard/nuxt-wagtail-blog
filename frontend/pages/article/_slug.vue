<template>
  <div>
    <article-view :article="article" />
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
          :offset="{ top: -380, bottom: 0 }"
          class="hidden-md-and-down"
        >
          TABLE OF CONTENT
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
import SupportAuthor from "../../components/blog/SupportAuthor";
import ShareCard from "../../components/blog/ShareCard";

export default {
  name: 'ArticlePage',
  middleware: 'increment-views',
  components: {
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
      article: {}
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
      }
    }
  }
}
</script>

<style scoped></style>
