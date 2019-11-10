<template>
  <v-row class="pt-6">
    <v-col cols="1" class="hidden-md-and-down">
      <v-btn icon :to="`/profile/${user.id}`" class="mt-2">
        <v-avatar>
          <v-img :src="formatAvatarUrl(user.avatar)" />
        </v-avatar>
      </v-btn>
    </v-col>
    <v-col cols="12" md="12" lg="11">
      <v-textarea
        v-model="text"
        placeholder="Новый комментарий"
        outlined
        auto-grow
        rounded
        class="mx-2"
        row-height="22"
        counter="3000"
        rows="2"
      >
        <template #append>
          <v-scroll-x-transition>
            <v-icon
              v-if="text.length > 0"
              color="primary"
              @click="createComment"
            >
              mdi-send
            </v-icon>
          </v-scroll-x-transition>
        </template>
      </v-textarea>
    </v-col>
  </v-row>
</template>

<script>
import { CREATE_COMMENT } from '../../graphql/comments/mutations'
import { GET_COMMENTS } from '../../graphql/comments/queries'
import { CURRENT_USER_CLIENT } from '../../graphql/users/queries'
import utilsMixin from '../../utils/utilsMixin'

export default {
  name: 'CommentInput',
  mixins: [utilsMixin],
  props: {
    modelName: {
      type: String,
      default: null
    },
    instanceId: {
      type: [Number, String],
      default: null
    },
    parentId: {
      type: [Number, String],
      default: null
    }
  },
  data() {
    return {
      text: '',
      user: {
        id: null,
        avatar: null
      }
    }
  },
  apollo: {
    user: {
      query: CURRENT_USER_CLIENT
    }
  },
  methods: {
    createComment() {
      const variables = {
        text: this.text,
        modelName: this.modelName,
        instanceId: this.instanceId,
        parentId: this.parentId
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
