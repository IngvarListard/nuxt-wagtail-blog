<template>
  <div>
    <div class="headline my-2">Комментарии {{ comments.length }}</div>
    <v-divider />
    <comment-input :model-name="modelName" :instance-id="instanceId" />
    <template v-if="comments.length > 0">
      <comment-block
        v-for="comment of comments"
        :key="comment.id"
        :comment="comment"
        :instance-id="instanceId"
      />
    </template>
    <div v-else class="headline ma-4">
      Здесь пока нет ни одного комментария...
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import { GET_COMMENTS } from '../../graphql/comments/queries'
import CommentBlock from './CommentBlock'
import CommentInput from './CommentInput'
export default {
  name: 'CommentsBlock',
  components: { CommentInput, CommentBlock },
  props: {
    modelName: {
      type: String,
      default: null
    },
    instanceId: {
      type: [Number, String],
      default: -1
    }
  },
  data() {
    return {
      comments: []
    }
  },
  apollo: {
    comments: {
      query: GET_COMMENTS,
      variables() {
        const instanceId = this.instanceId
        const modelName = this.modelName
        const skip = 0
        const first = 20
        return {
          instanceId,
          modelName,
          skip,
          first
        }
      },
      update({ comments }) {
        console.log(comments)
        const commentsCopy = _.cloneDeep(comments.comments)
        commentsCopy.forEach(comment => {
          this.$set(comment, 'showReplyBox', false)
        })
        return commentsCopy
      },
      skip() {
        return !this.instanceId || !this.modelName
      }
    }
  }
}
</script>

<style scoped></style>
