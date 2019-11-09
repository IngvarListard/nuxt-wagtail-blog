<template>
  <v-card flat>
    <v-card-text class="my-1 py-2">
      <v-row dense>
        <v-col cols="1">
          <v-avatar>
            <v-img v-if="test(comment)" :src="formatAvatarUrl(comment.user.avatar)" alt="Avatar" />
          </v-avatar>
        </v-col>
        <v-col cols="11">
          <div class="text--primary">
            <div class="mb-2">
              <strong style="font-size: 18px;">{{
                comment.user.displayName
              }}</strong>
              {{ formatCommentDate(comment.time) }}
            </div>
            <comment :text="comment.text" style="font-size: 16px;" />
          </div>
          <span
            style="cursor: pointer;"
            @click="comment.showReplyBox = !comment.showReplyBox"
            >Ответить</span
          >
          <vote-counter
            :instance-id="comment.id"
            :votes-count="comment.votesCount"
            model-name="comments.Comment"
          />
          <v-slide-y-transition>
            <comment-input
              v-if="comment.showReplyBox"
              model-name="comments.comment"
              :instance-id="instanceId"
              :parent-id="comment.id"
            />
          </v-slide-y-transition>
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
import utilsMixin from '../../utils/utilsMixin'
import VoteCounter from '../widgets/VoteCounter'
import Comment from './Comment'
import CommentInput from './CommentInput'

export default {
  name: 'CommentBlock',
  components: { CommentInput, VoteCounter, Comment },
  mixins: [utilsMixin],
  props: {
    comment: {
      type: Object,
      default: () => ({
        id: -1,
        text: '',
        parent: null,
        user: {
          id: -1,
          displayName: 'Guest',
          avatar: null
        },
        time: null,
        votesCount: { likes: 0, dislikes: 0, userVote: null },
        childCount: 0
      })
    },
    instanceId: {
      type: [Number, String],
      default: null
    }
  },
  methods: {
    test(data) {
      return true
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
