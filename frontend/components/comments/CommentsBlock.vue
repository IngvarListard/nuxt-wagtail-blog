<template>
  <div>
    <div class="headline my-2">Комментарии 2817</div>
    <v-divider />
    <comment-input />
    <comment-block v-if="comments.length > 0" />
    <div v-else class="headline ma-4">
      Здесь пока нет ни одного комментария...
    </div>
  </div>
</template>

<script>
import CommentBlock from './CommentBlock'
import CommentInput from './CommentInput'
import { GET_COMMENTS } from '../../graphql/comments/query'
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
      }
    }
  }
}
</script>

<style scoped></style>
