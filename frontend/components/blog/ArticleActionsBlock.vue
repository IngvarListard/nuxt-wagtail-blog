<template>
  <v-card outlined>
    <table>
      <tr>
        <td>
          <vote-counter
            :instance-id="instanceId"
            :count="votesCount"
            model-name="blog.BlogPage"
          />
        </td>
<!--        <td>-->
<!--          <bookmark :count="bookmarkCount" />-->
<!--        </td>-->
        <td>
          <views-counter :count="viewsCount" />
        </td>
        <td>
          <comment-counter :count="commentsCount" />
        </td>
      </tr>
    </table>
  </v-card>
</template>

<script>
import VoteCounter from '../widgets/VoteCounter'
import Bookmark from '../widgets/Bookmark'
import ViewsCounter from '../widgets/ViewsCounter'
import CommentCounter from '../widgets/CommentCounter'
export default {
  name: 'ArticleActionsBlock',
  components: { CommentCounter, ViewsCounter, Bookmark, VoteCounter },
  props: {
    instanceId: {
      type: [Number, String],
      required: true,
      default: 0
    },
    votesCount: {
      type: Object,
      required: true,
      default: () => ({
        likes: 0,
        dislikes: 0,
        userVote: null
      })
    },
    viewsCount: {
      type: Number,
      required: true,
      default: 0
    },
    commentsCount: {
      type: Number,
      required: true,
      default: 0
    },
    bookmarkCount: {
      type: Number,
      required: true,
      default: 0
    }
  }
}
</script>

<style scoped>
th,
td {
  padding: 5px;
}
</style>
