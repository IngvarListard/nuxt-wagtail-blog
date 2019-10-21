<template>
  <div>
    <v-btn @click="test">test</v-btn>
    <div v-for="(item, key) of todoItems" :key="key">
      {{ item.text }}
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'Test',
  data() {
    return {
      allUsers: null,
      todoItems: [],
      shit: 0,
      checkItemMutation: gql`
        mutation($id: ID!) {
          checkItem(id: $id) @client
        }
      `
    }
  },
  apollo: {
    todoItems: {
      query: gql`
        {
          todoItems @client {
            id
            text
            done
          }
        }
      `,
      prefetch: false
    }
  },
  methods: {
    test() {
      this.$apollo.provider.defaultClient.writeData({
        data: {
          todoItems: [
            ...this.todoItems,
            {
              __typename: 'Item',
              id: `dqdBHJGgjgjg${this.shit++}`,
              text: `test ${this.shit}`,
              done: true
            }
          ]
        }
      })
    }
  }
}
</script>

<style scoped></style>
