<template>
  <div>
    <v-row>
      <v-col
        v-for="activity of events"
        :key="activity.id"
        cols="12"
        lg="6"
        md="6"
        sm="12"
      >
        <event-card :activity="activity" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import EventCard from '../components/events/EventCard'

export default {
  name: 'Events',
  components: { EventCard },
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
  }
}
</script>

<style scoped></style>
