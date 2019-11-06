<template>
  <v-container fluid>
    <v-row>
      <v-col v-for="event in events" xs="12" md="6" lg="4" xl="3">
        <v-card @click="openEvent(event)">
          <v-img
            class="white--text align-end"
            height="200px"
            :src="event.image ? event.image.original : ''"
          >
          </v-img>
          <v-card-subtitle class="pb-0">
            {{ convertDateTime(event.start_date) }}
          </v-card-subtitle>
          <v-card-text class="text--primary">
            <div>{{event.name}}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import gql from 'graphql-tag'
import axios from 'axios'


export default {
  name: 'events',
  data() {
    return {
      events: []
    }
  },
  apollo: {
    query: {
      query: gql`
        query {
          getEventsPaged
        }
      `,
      update(data) {
        this.events = JSON.parse(data.getEventsPaged).results
      }
    }
  },
  methods: {
    convertDateTime(dateTime) {
      let monthes = [
        'Января',
        'Февраля',
        'Марта',
        'Апреля',
        'Мая',
        'Июня',
        'Июля',
        'Августа',
        'Сентября',
        'Октября',
        'Ноября',
        'Декабря'
      ]

      dateTime = new Date(dateTime)
      let day = dateTime.getDate()
      let month = monthes[dateTime.getMonth()]
      let year = dateTime.getFullYear()
      return `${day} ${month} ${year}`
    },
    openEvent(event) {
      let url = "https://добровольцыроссии.рф/organizations/1?event=" + event.slug
      window.open(url, '_blank')
    }
  },
}
</script>

<style scoped>

</style>
