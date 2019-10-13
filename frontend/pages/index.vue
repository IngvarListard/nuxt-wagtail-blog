<template>
  <div>
    <v-row class="mx-0">
      <v-img
        :src="
          require('@/assets/banner.jpeg')
        "
        width="100%"
        max-height="30%"
        aspect-ratio="4.5"
      ></v-img>
    </v-row>
    <v-container>
      <v-row justify="space-around">
        <v-col md="6" class="mx-4" sm="12">
          <v-card v-for="k of 10" class="my-12"  outlined>
            <v-img :src="require('@/assets/whereis1.png')" aspect-ratio="2.5">
            </v-img>

            <v-container class="px-10">
              <v-card-title
                style="font-size: 48px; line-height: 1.2"
                class="pt-12 pb-8 px-10 text-center"
              >
                <div style="text-align: center;">
                  Wagtail and Azure Storage Blob Containers
                </div>
              </v-card-title>
              <v-divider class="mb-5 px-10" />
              <v-icon>mdi-calendar</v-icon> 2 октября 2019 \
              <v-icon>mdi-account-outline</v-icon> admin \
              <v-chip label
                ><v-icon class="mr-2">mdi-tag-outline</v-icon>Спорт</v-chip
              >
              <v-chip label
                ><v-icon class="mr-2">mdi-tag-outline</v-icon>Отдых</v-chip
              >
              <v-chip label
                ><v-icon class="mr-2">mdi-tag-outline</v-icon>Туризм</v-chip
              >
              <v-card-text
                style="font-size: 22px; line-height: 1.7;"
                class="px-10"
              >
                So recently I've been working on a project to move old legacy
                sites into Wagtail and we've set this Wagtail site up on the
                Azure Cloud using Azure Web Apps for Linux with a custom Docker
                Container. Ideally we wanted images uploaded by the user and our
                static files stored separately so we used Azure …

                <v-spacer />
                <v-btn color="blue-grey" text x-large class="mx-4 my-4"
                  >Читать далее</v-btn
                >
              </v-card-text>
            </v-container>
            <v-card-actions>
              <v-icon large class="mx-4">mdi-heart</v-icon>
              <span style="color: slategrey; font-size: 22px;">69</span>
              <v-icon large class="mx-4">mdi-eye</v-icon>
              <span style="color: slategrey; font-size: 22px;">230</span>
              <v-icon large class="mx-4">mdi-comment</v-icon>
              <span style="color: slategrey; font-size: 22px;">3</span>
            </v-card-actions>
            <v-card-actions> </v-card-actions>
          </v-card>
        </v-col>
        <v-col md="3" class="mx-4" sm="12">
          <v-text-field
            append-icon="mdi-magnify"
            outlined
            placeholder="Искать на сайте"
            clearable
            class="pt-12"
          />
          <categories />
          <best-widget class="my-2"/>
          <newsletter-subscribe class="my-2"/>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import BestWidget from '../components/common/home/BestWidget'
import NewsletterSubscribe from '../components/common/home/NewsletterSubscribe'
import Categories from '../components/common/home/Categories'
import { allUsers } from '~/graphql/users/queries'

export default {
  components: { BestWidget, NewsletterSubscribe, Categories },
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
