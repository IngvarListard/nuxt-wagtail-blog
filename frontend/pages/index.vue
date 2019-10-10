<template>
  <div>
    <v-row class="mx-0">
      <v-img
        :src="require('@/assets/banner_linux2.jpg')"
        width="100%"
        max-height="30%"
      ></v-img>
    </v-row>
    <v-container>
      <v-row justify="center">
        <v-col md="7" class="mx-4" sm="12">
          <v-card v-for="k of 10" class="mt-4">
            <v-row>
              <v-col md="6" sm="12" class="py-0">
                <v-img :src="require('@/assets/whereis1.png')"> </v-img>
              </v-col>

              <v-col md="6" sm="12">
                <v-card-title>TITLE title</v-card-title>
                <v-card-text style="font-size: 18px">
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. A
                  aliquam aut dignissimos iusto sequi. Ab debitis ea impedit
                  laborum natus neque nesciunt odit ullam voluptatum. Libero
                  natus non perferendis placeat?
                </v-card-text>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
        <v-col md="3" class="mx-4" sm="12">
          <v-card v-for="m of 10" class="mt-4">
            <v-card-title>
              bbbbbb
            </v-card-title>
            <v-card-text>
              bbbbbb
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
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
      console.log(this.$vuetify)
      console.log(this.$vueport)
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
