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
          }
        })
        .then(() => {})
        .catch(e => {})
    }
  }
}
</script>

<style scoped></style>
