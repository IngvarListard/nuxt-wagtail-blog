<template>
  <div>
    <div class="display-3 mb-3">Случайная статья</div>
    <random-article />
    <portal to="bottom">
      <feed />
    </portal>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import RandomArticle from '../components/blog/RandomArticle'
import Feed from '../components/blog/Feed'
import { allUsers } from '~/graphql/users/queries'

export default {
  components: { RandomArticle, Feed },
  data() {
    return {
      allUsers: [],
      file: null
    }
  },
  apollo: {
    allUsers: {
      query: allUsers,
      subscribeToMore: {
        document: gql`
          subscription mySubscription($arg1: String, $arg2: String) {
            mySubscription(arg1: $arg1, arg2: $arg2) {
              event
            }
          }
        `,
        skip() {
          return process.server
        },
        variables() {
          return {
            arg1: 'test',
            arg2: 'another test'
          }
        }
      },
      update(data) {
        return data.allUsers
      },
      prefetch: false
    }
  }
}
</script>
