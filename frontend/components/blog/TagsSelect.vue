<template>
  <v-combobox
    v-model="selectedTags"
    placeholder="Выберите тэги"
    :items="tags"
    :loading="loading > 0 || initLoading"
    outlined
    flat
    multiple
    small-chips
    solo
    hide-details
    clearable
    class="my-0 py-0"
  >
    <template v-slot:selection="{ attrs, item, parent, selected, index }">
      <v-chip
        v-if="index <= 1"
        v-bind="attrs"
        :color="`${item.color} lighten-3`"
        :input-value="selected"
        label
        small
      >
        <span class="pr-2">
          {{ item }}
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
import _ from 'lodash'
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
      initLoading: false,
      tags: [],
      selectedTags: [],
      tagsList: []
    }
  },
  apollo: {
    tags: {
      query: GET_PAGED_TAGS,
      variables() {
        const search = this.search
        const page = this.page
        const perPage = this.perPage
        const tagsList = this.tagsList
        return { search, page, perPage, tagsList }
      },
      debounce: 500,
      loadingKey: 'loading',
      update(data) {
        this.hasNext = data.tagsPage.hasNext
        return data.tagsPage.tags.map(tag => tag.tag.name)
      }
    }
  },
  watch: {
    selectedTags(newVal) {
      const tags = newVal
      const query = _.cloneDeep(this.$route.query)
      query.tags = tags
      this.$router.push({
        name: 'search',
        query
      })
      this.$emit('input', tags)
    },
    /**
     * Данный вотч нужен на случай, если тэг в запрос route'a будет передаваться извне.
     * @param newVal
     */
    '$route.query'(newVal) {
      if (newVal.tags) {
        const tags = _.isArray(newVal.tags) ? newVal.tags : [newVal.tags]
        this.selectTags(tags)
      }
    }
  },
  mounted() {
    // после маунта компонента добавляем тэги из
    // строки запроса в выбранные
    let tags = this.$route.query.tags
    if (tags) {
      tags = _.isArray(tags) ? tags : [tags]
      this.selectTagsAfterApollo(tags)
    }
  },
  methods: {
    /**
     * Функция для подхватывания тэгов после маунта компонента.
     * Ожидает первичной загрузки apollo, после этого запускает
     * функцию обработки (добавления или дозагрузки) тэгов.
     * @param tags
     */
    selectTagsAfterApollo(tags) {
      this.initLoading = true
      if (
        this.$apollo.queries.tags.loading ||
        this.$apollo.queries.tags.starting
      ) {
        setTimeout(() => {
          this.selectTagsAfterApollo(tags)
        }, 400)
      } else {
        this.selectTags(tags)
        this.initLoading = false
      }
    },
    /**
     * Добавляет тэги из массива tags в selectedTags, если
     * такие тэги есть в массиве tags. Если нет, то догружает
     * с бэка.
     * @param tags {Array}
     */
    selectTags(tags) {
      const isEqual = _.isEqual(
        _.sortBy(tags || []),
        _.sortBy(this.selectedTags)
      )
      if (isEqual) return
      const difference = _.difference(
        _.sortBy(tags || []),
        _.sortBy(this.selectedTags)
      )
      if (difference.length === 0) return
      const newTags = []
      tags.forEach(tag => {
        if (this.tags.indexOf(tag) !== -1) {
          this.selectedTags = [tag]
          newTags.push(tag)
        }
      })
      if (newTags.length > 0) this.selectedTags = newTags
      const probablyUnloadedTags = _.difference(newTags, this.tags)
      if (probablyUnloadedTags.length === 0) {
        return
      }
      return this.$apollo.queries.tags
        .fetchMore({
          variables: {
            page: this.page,
            perPage: this.perPage,
            tagsList: probablyUnloadedTags
          },
          updateQuery: (previousResult, { fetchMoreResult }) => {
            const newTags = fetchMoreResult.tagsPage.tags
            const hasNext = previousResult.tagsPage.hasNext
            return {
              tagsPage: {
                __typename: previousResult.tagsPage.__typename,
                hasNext,
                tags: _.uniq([...newTags, ...previousResult.tagsPage.tags])
              }
            }
          }
        })
        .then(({ data: { tagsPage: { tags } } }) => {
          // вставляем в выборку дозагруженные тэги
          this.selectedTags = this.selectedTags.concat(
            tags.map(tag => tag.tag.name)
          )
        })
    },
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
