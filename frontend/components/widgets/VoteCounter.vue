<template>
  <span>
    <v-btn text icon class="mr-2" v-bind="options" @click="vote('like')"
      ><v-icon v-bind="options" :color="thumbColor.like"
        >mdi-thumb-up-outline</v-icon
      ></v-btn
    ><span
      class="font-weight-regular mr-2"
      style="font-size: 16px; color: #999999;"
      >{{ count.likes }}</span
    >
    <v-btn icon class="mr-2" v-bind="options" @click="vote('dislike')"
      ><v-icon v-bind="options" :color="thumbColor.dislike"
        >mdi-thumb-down-outline</v-icon
      ></v-btn
    ><span
      class="font-weight-regular"
      style="font-size: 16px; color: #999999;"
      >{{ count.dislikes }}</span
    >
  </span>
</template>

<script>
import { defaultDataIdFromObject } from 'apollo-cache-inmemory'
import { TO_VOTE } from '../../graphql/votes/mutations'
import { ARTICLE_VOTES_FRAGMENT } from '../../graphql/blog/fragments'

export default {
  name: 'VoteCounter',
  props: {
    options: {
      type: Object,
      default: () => ({})
    },
    count: {
      type: Object,
      default: () => ({ likes: 0, dislikes: 0, userVote: null })
    },
    instanceId: {
      type: [Number, String],
      default: null
    },
    /**
     * @param {String} modelName - К какой модели будут применяться голоса:
     *  - 'blog.BlogPage'
     *  - 'comments.Comment'
     */
    modelName: {
      type: String,
      default: null
    }
  },
  computed: {
    thumbColor() {
      const like = this.count.userVote === 'like' ? 'success' : null
      const dislike = this.count.userVote === 'dislike' ? 'success' : null
      return {
        like,
        dislike
      }
    }
  },
  methods: {
    vote(action) {
      const instanceId = this.instanceId
      const modelName = this.modelName
      this.$apollo
        .mutate({
          mutation: TO_VOTE,
          variables: {
            instanceId,
            action,
            modelName
          },
          update: (store, { data: { vote } }) => {
            // для примера использования readFragment
            // это останется здесь пока не пригодится!!!
            const instance = store.readFragment({
              id: defaultDataIdFromObject({
                id: instanceId,
                __typename: 'ArticleNode'
              }),
              fragment: ARTICLE_VOTES_FRAGMENT
            })
          }
        })
        .then(voteCount => {})
        .catch(e => {})
    }
  }
}
</script>

<style scoped></style>
