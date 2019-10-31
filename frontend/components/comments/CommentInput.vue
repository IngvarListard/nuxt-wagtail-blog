<template>
  <v-row>
    <v-icon x-large class="mx-2">mdi-account-circle-outline</v-icon>
    <v-textarea
      v-model="text"
      placeholder="Новый комментарий"
      outlined
      class="pt-6 px-2"
      auto-grow
      rounded
      row-height="22"
      counter="3000"
      rows="2"
    >
      <template #append>
        <v-scroll-x-transition>
          <v-icon v-if="text.length > 0" color="primary" @click="createComment">
            mdi-send
          </v-icon>
        </v-scroll-x-transition>
      </template>
    </v-textarea>
  </v-row>
</template>

<script>
import { CREATE_COMMENT } from '../../graphql/comments/mutations'
import { GET_COMMENTS } from '../../graphql/comments/queries'

export default {
  name: 'CommentInput',
  props: {
    modelName: {
      type: String,
      default: null
    },
    instanceId: {
      type: [Number, String],
      default: -1
    },
    parentId: {
      type: [Number, String],
      default: null
    }
  },
  data() {
    return {
      text: ''
    }
  },
  methods: {
    createComment() {
      const variables = {
        text: this.text,
        modelName: this.modelName,
        instanceId: this.instanceId
      }
      this.$apollo
        .mutate({
          mutation: CREATE_COMMENT,
          variables,
          update: (
            store,
            {
              data: {
                createComment: { comment }
              }
            }
          ) => {
            variables.skip = 0
            variables.first = 20
            const data = store.readQuery({
              query: GET_COMMENTS,
              variables
            })
            data.comments.comments.unshift(comment)
            store.writeQuery({ query: GET_COMMENTS, variables, data })
          }
        })
        .then(() => {
          this.text = ''
        })
        .catch(e => {
          this.text = ''
          throw new Error(e)
        })
    }
  }
}
</script>

<style scoped></style>
