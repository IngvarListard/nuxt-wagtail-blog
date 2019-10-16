<template>
  <div>
    <v-container>
      <v-row justify="center">
        <v-col lg="7" md="12" sm="12">
          <div class="display-3 mb-3">Real Python Tutorials</div>
          <random-article />
        </v-col>
        <v-col lg="3" md="12" sm="12">
          <newsletter-subscribe />
          <tags-card class="my-4" />
        </v-col>
      </v-row>
      <feed />
    </v-container>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import NewsletterSubscribe from '../components/common/home/NewsletterSubscribe'
import TagsCard from '../components/common/home/TagsCard'
import RandomArticle from '../components/common/home/RandomArticle'
import Feed from '../components/common/home/Feed'
import { allUsers } from '~/graphql/users/queries'

export default {
  components: { NewsletterSubscribe, TagsCard, RandomArticle, Feed },
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
  },
  computed: {
    responsiveClasses() {
      return {}
    },
    responsiveStyles() {
      return {}
    }
  },
  methods: {}
}
</script>
