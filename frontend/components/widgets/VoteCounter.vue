<template>
  <span>
    <v-btn text icon class="mr-2" v-bind="options" @click="vote('like')"
      ><v-icon v-bind="options">mdi-thumb-up-outline</v-icon></v-btn
    ><span class="mr-2">{{ votesCount.likes }}</span>
    <v-btn icon class="mr-2" v-bind="options" @click="vote('dislike')"
      ><v-icon v-bind="options">mdi-thumb-down-outline</v-icon></v-btn
    ><span>{{ votesCount.dislikes }}</span>
  </span>
</template>

<script>
import { VOTE_ARTICLE } from '../../graphql/votes/mutations'
import { ARTICLE_VOTES_FRAGMENT } from '../../graphql/blog/fragments'
import { defaultDataIdFromObject } from 'apollo-cache-inmemory'

export default {
  name: 'VoteCounter',
  props: {
    options: {
      type: Object,
      default: () => ({ small: true })
    },
    votesCount: {
      type: Object,
      default: () => ({ likes: 0, dislikes: 0, userVote: null })
    },
    articleId: {
      type: [Number, String],
      default: null
    }
  },
  methods: {
    vote(action) {
      const articleId = this.articleId
      this.$apollo
        .mutate({
          mutation: VOTE_ARTICLE,
          variables: {
            articleId,
            action
          },
          update: (store, { data: { vote } }) => {
            // для примера использования readFragment
            const article = store.readFragment({
              id: defaultDataIdFromObject({
                id: articleId,
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
