<template>
  <v-card flat>
    <v-card-text>
      <v-row align="top">
        <v-col cols="1">
          <v-avatar>
            <v-img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="test" />
          </v-avatar>
        </v-col>
        <v-col cols="11">
          <div class="text--primary">
            <strong>Членов Иван Иванович</strong> 13 дней отредактировано<br />
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci
            beatae delectus dolor dolore id, illum itaque iure laudantium,
            libero minus necessitatibus nesciunt, non numquam recusandae
            suscipit unde velit vero? Omnis? Lorem ipsum dolor sit amet,
            consectetur adipisicing elit. Delectus dolorum esse inventore
            quibusdam veritatis voluptatem. Aspernatur excepturi itaque libero
            nihil non voluptates. Adipisci at blanditiis consequatur
            dignissimos, neque unde vitae. beatae delectus dolor dolore id,
            illum itaque iure laudantium, libero minus necessitatibus nesciunt,
            non numquam recusandae suscipit unde velit vero? Omnis? Lorem ipsum
            dolor sit amet, consectetur adipisicing elit. Delectus dolorum esse
            inventore quibusdam veritatis voluptatem. Aspernatur excepturi
            itaque libero nihil non voluptates. Adipisci at blanditiis
            consequatur dignissimos, neque unde vitae. beatae delectus dolor
            dolore id, illum itaque iure laudantium, libero minus necessitatibus
            nesciunt, non numquam recusandae suscipit unde velit vero? Omnis?
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus
            dolorum esse inventore quibusdam veritatis voluptatem. Aspernatur
            excepturi itaque libero nihil non voluptates. Adipisci at blanditiis
            consequatur dignissimos, neque unde vitae.
          </div>
          Ответить
          <vote-counter
            :instance-id="comment.id"
            :votes-count="comment.votesCount"
            vote-to="comments.Comment"
          />
          <br />
          <v-icon class="icon-flipped my-2">mdi-keyboard-return</v-icon>
          <strong class="text--primary">354 ответа</strong>
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
        votes: { likes: 0, dislikes: 0, userVote: null }
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
