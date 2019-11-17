<template>
  <div>
    <yandex-map ref="yandexMap" :coords="coords" :zoom="zoom" class="event-map" @click="onClick">
      <ymap-marker
        v-for="(event, index) in events"
        :coords="[events[index].x, events[index].y]"
        :hint-content="events[index].description"
        :balloon-template="card(event)"
        :marker-id="events[index].id"
      />

      <ymap-marker
        v-if="myCoords"
        :coords="myCoords"
        marker-id="123"
        :icon="{content: 'Вы здесь'}"
      />
    </yandex-map>

    <v-btn
      :loading="loading"
      :disabled="loading"
      class="find-event"
      small
      color="#ffdb4d"
      @click="findEvents"
    >
      Найти мероприятия
      <v-icon small>
        search
      </v-icon>
    </v-btn>

    <v-btn
      small
      class="define-my-position"
      color="#ffdb4d"
      @click="defineMyPosition"
    >
      Мое расположение
      <v-icon small>
        mdi-map-marker
      </v-icon>
    </v-btn>
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'EventMap',
  data() {
    return {
      coords: [48.67958009389022, 44.461972603156845],
      zoom: 12,
      myCoords: null,
      loading: false,
      events: []
    }
  },
  layout: 'default_for_map',
  methods: {
    defineMyPosition() {
      navigator.geolocation.getCurrentPosition(pos => {
        this.myCoords = [pos.coords.latitude, pos.coords.longitude]
        this.coords = this.myCoords
      })
    },
    findEvents() {
      this.loading = true
      this.$apollo
        .query({
          query: gql`
            query($x: Float, $y: Float) {
              getEventsByPosition(x: $x, y: $y) {
                id
                x
                y
                address
                description
                name
                slug
                imageUrl
                date
              }
            }
          `,
          variables: {
            x: this.coords[0],
            y: this.coords[1]
          }
        })
        .then(data => {
          this.events = data.data.getEventsByPosition
          this.zoom = 12
          this.loading = false
        })
    },
    onClick(e) {
      this.coords = e.get('coords')
    },
    card(event) {
      let rusDate = event.date.split('-').reverse().join('.')
      let url = 'https://добровольцыроссии.рф/organizations/1?event='
      return `
        <v-card>
          <v-card-text>
          <a style="color: black; text-decoration: none;" href="${url}${event.slug}" target="_blank">
            <img
              style="width: 380px"
              src="${event.imageUrl}"
            />
            <div>
              <h2>${event.name}</h2>
            </div>
            <div style="color:grey;font-size:85%;">
              ${rusDate}
            </div>
            <div>
              ${event.description}
            </div>
          </a>

          </v-card-text>
        </v-card>
      `
    }
  }
}
</script>

<style scoped>
.event-map {
  position: fixed;
  top: 62px;
  left: 0;
  right: 0;
  bottom: 0;
}

.find-event {
  position: fixed;
  top: 72px;
  left: 370px;
  font-size: 13px;
}

.define-my-position {
  position: fixed;
  top: 72px;
  left: 581px;
  font-size: 13px;
}
</style>
