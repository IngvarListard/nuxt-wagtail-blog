<template>
  <div>
    <p>{{ article.date }}</p>
    <h2>{{ article.title }}</h2>
    <div>{{ article.intro }}</div>
    <div v-for="body of article.body" :key="body.id">
<!--      <div v-html></div>-->
      {{ body.value }}
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'Article',
  apollo: {
    article: {
      query: gql`
        query($articleId: ID!) {
          article(articleId: $articleId) {
            id
            title
            date
            intro
            body
          }
        }
      `,
      variables() {
        return {
          articleId: this.$route.params.id
        }
      }
    }
  }
}
</script>

<style scoped></style>
