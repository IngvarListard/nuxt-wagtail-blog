<template>
  <v-combobox
    v-model="selectedTags"
    placeholder="Выберите тэги"
    :items="tags"
    item-text="tag.name"
    item-value="tag.name"
    :loading="loading > 0"
    outlined
    flat
    multiple
    small-chips
    solo
    hide-details
    class="my-0 py-0"
  >
    <template v-slot:selection="{ attrs, item, parent, selected, index }">
      <v-chip
        v-if="item === Object(item) && index <= 1"
        v-bind="attrs"
        :color="`${item.color} lighten-3`"
        :input-value="selected"
        label
        small
      >
        <span class="pr-2">
          {{ item.tag.name }}
        </span>
        <v-icon small @click="parent.selectItem(item)">close</v-icon>
      </v-chip>
      <span v-if="index === 2" class="grey--text caption"
        >(+{{ selectedTags.length - 2 }} ещё)</span
      >
    </template>
    <template v-slot:append-item>
      <div v-intersect.quiet="onIntersect" class="text-center">
        <v-progress-circular v-if="loading > 0" size="60" indeterminate />
      </div>
    </template>
  </v-combobox>
</template>

<script>
import { GET_PAGED_TAGS } from '../../graphql/blog/queries'

export default {
  name: 'TagsSelect',
  props: {
    value: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      page: 1,
      perPage: 10,
      hasNext: true,
      search: '',
      loading: 0,
      tags: [],
      selectedTags: []
    }
  },
  apollo: {
    tags: {
      query: GET_PAGED_TAGS,
      variables() {
        const search = this.search
        const page = this.page
        const perPage = this.perPage
        return { search, page, perPage }
      },
      debounce: 500,
      loadingKey: 'loading',
      update(data) {
        this.hasNext = data.tagsPage.hasNext
        return data.tagsPage.tags
      }
    }
  },
  watch: {
    selectedTags(newVal) {
      this.$emit('input', newVal.map(i => i.tag.name))
    }
  },
  methods: {
    onIntersect(entries, observer, isIntersecting) {
      if (this.$apollo.queries.tags.loading || !isIntersecting || !this.hasNext)
        return
      this.page++
      this.$apollo.queries.tags.fetchMore({
        variables: {
          page: this.page,
          perPage: this.perPage,
          search: this.search
        },
        updateQuery: (previousResult, { fetchMoreResult }) => {
          const newTags = fetchMoreResult.tagsPage.tags
          const hasNext = fetchMoreResult.tagsPage.hasNext
          this.hasNext = hasNext
          return {
            tagsPage: {
              __typename: previousResult.tagsPage.__typename,
              hasNext,
              tags: [...previousResult.tagsPage.tags, ...newTags]
            }
          }
        }
      })
    }
  }
}
</script>

<style scoped></style>
