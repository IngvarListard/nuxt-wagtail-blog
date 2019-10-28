<template>
  <div>
    <div class="headline my-2">Комментарии 2817</div>
    <v-divider />
    <v-row align="top">
      <v-icon x-large class="mx-2">mdi-account-circle-outline</v-icon>
      <v-textarea
        v-model="text"
        label="Новый комментарий"
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
            <v-icon
              v-if="text.length > 0"
              color="primary"
              @click=""
            >
              mdi-send
            </v-icon>
          </v-scroll-x-transition>
        </template>
      </v-textarea>
    </v-row>
    <v-card flat>
      <v-card-text>
        <v-row align="top">
          <v-col cols="1">
            <v-avatar>
              <v-img
                src="https://cdn.vuetifyjs.com/images/john.jpg"
                alt="test"
              />
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
              illum itaque iure laudantium, libero minus necessitatibus
              nesciunt, non numquam recusandae suscipit unde velit vero? Omnis?
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus
              dolorum esse inventore quibusdam veritatis voluptatem. Aspernatur
              excepturi itaque libero nihil non voluptates. Adipisci at
              blanditiis consequatur dignissimos, neque unde vitae. beatae
              delectus dolor dolore id, illum itaque iure laudantium, libero
              minus necessitatibus nesciunt, non numquam recusandae suscipit
              unde velit vero? Omnis? Lorem ipsum dolor sit amet, consectetur
              adipisicing elit. Delectus dolorum esse inventore quibusdam
              veritatis voluptatem. Aspernatur excepturi itaque libero nihil non
              voluptates. Adipisci at blanditiis consequatur dignissimos, neque
              unde vitae.
            </div>
            Ответить
            <vote-counter />
            <br />
            <v-icon class="icon-flipped my-2">mdi-keyboard-return</v-icon>
            <strong class="text--primary">354 ответа</strong>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import VoteCounter from '../widgets/VoteCounter'
export default {
  name: 'CommentsBlock',
  components: { VoteCounter },
  data() {
    return {
      text: ''
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
