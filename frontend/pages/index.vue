<template>
  <div>
    <v-btn @click="test">TEST</v-btn>
    <v-btn @click="notif">TEST2</v-btn>
    <v-btn @click="socketTest">TEST3</v-btn>
    <div>
      <v-file-input v-model="file" />
      <v-btn @click="fileUpload">UPLOAD FILE</v-btn>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { allUsers } from '~/graphql/users/queries'

export default {
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
  methods: {
    test() {
      this.$apollo
        .query({
          query: allUsers,
          fetchPolicy: 'no-cache'
        })
        .then(({ data }) => {
          this.allUsers = data.allUsers
        })
    },
    notif() {},
    socketTest() {
      this.$socket.sendObj({ message: 'aaaa' })
    },
    fileUpload() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation($file: Upload!) {
              fileUpload(file: $file) {
                success
              }
            }
          `,
          variables: {
            file: this.file
          },
          context: {
            hasUpload: true // activate Upload link
          }
        })
        .then(({ data }) => {
          console.log(data)
        })
    }
  }
}
</script>
