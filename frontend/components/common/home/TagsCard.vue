<template>
  <v-card outlined>
    <v-card-title style="font-size: 23px" class="font-weight-light pt-2 px-3"
      >Тэги</v-card-title
    >
    <v-card-text class="px-3">
      <tag v-for="tag of tags" :key="tag.id" :tag="tag" class="ml-1" />
    </v-card-text>
  </v-card>
</template>

<script>
import Tag from '../../widgets/Tag'
import { TAGS } from '../../../graphql/blog/queries'

export default {
  name: 'TagsCard',
  components: {
    Tag
  },
  data() {
    return {
      tags: []
    }
  },
  apollo: {
    tags: {
      query: TAGS
    }
  }
}
</script>

<style scoped></style>
