<template>
  <v-card flat>
    <v-card-text class="my-1 py-2">
      <v-row dense>
        <v-col cols="1">
          <v-avatar>
            <v-img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="test" />
          </v-avatar>
        </v-col>
        <v-col cols="11">
          <div class="text--primary">
            <div class="mb-2">
              <strong style="font-size: 18px;">{{
                comment.user.displayName
              }}</strong>
              {{ comment.time }}
            </div>
            {{ comment.text }}
          </div>
          Ответить
          <vote-counter
            :instance-id="comment.id"
            :votes-count="comment.votesCount"
            model-name="comments.Comment"
          />
          <br />
          <template v-if="comment.childCount > 0">
            <v-icon class="icon-flipped my-2">mdi-keyboard-return</v-icon>
            <strong class="text--primary"
              >{{ comment.childCount }} ответа</strong
            >
          </template>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import VoteCounter from '../widgets/VoteCounter'
export default {
  name: 'CommentBlock',
  components: { VoteCounter },
  props: {
    comment: {
      type: Object,
      default: () => ({
        id: -1,
        text: '',
        parent: null,
        user: {
          id: -1,
          displayName: 'Guest'
        },
        time: null,
        votesCount: { likes: 0, dislikes: 0, userVote: null },
        childCount: 0
      })
    }
  }
}
</script>

<style scoped>
.icon-flipped {
  transform: scaleX(-1);
  -moz-transform: scaleX(-1);
  -webkit-transform: scaleX(-1);
  -ms-transform: scaleX(-1);
}
</style>
