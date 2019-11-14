<template>
  <div>
    <yandex-map
      :coords.sync="coords"
      class="event-map"
      @click="onClick"
    >
      <template v-for="event in events">
        <ymap-marker
          :coords="event.coords"
          :hint-content="event.description"
          :market-id="event.id"
        />
      </template>

    </yandex-map>

    <v-btn
      @click="findEvents"
      :loading="loading"
      :disabled="loading"
      class="find-event"
      small
      color="#ffdb4d"
    >
      Найти мероприятия
      <v-icon small>
        search
      </v-icon>
    </v-btn>

    <v-btn
      @click="defineMyPosition"
      small
      class="define-my-position"
      color="#ffdb4d"
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
  name: 'event_map',
  data() {
    return {
      coords: [54, 39],
      loading: false,
      events: [{
        id: 1,
        coords: [0, 0]
      }, {
        id: 2,
        coords: [10, 10]
      }],
    }
  },
  methods: {
    defineMyPosition() {
      navigator.geolocation.getCurrentPosition(pos => {
        this.coords = [pos.coords.latitude, pos.coords.longitude]
      })
    },
    findEvents() {
      this.loading = true

      this.$apollo.query({
        query: gql`
          query($x: Float, $y:Float){
            getEventsByPosition(x: $x, y:$y)
          }
        `,
        variables: {
          x: this.coords[0],
          y: this.coords[1]
        }
      }).then(data => {
        this.events = JSON.parse(data.data.getEventsByPosition)
        // this.event = this.events[0]
        console.log(JSON.parse(data.data.getEventsByPosition))
        this.loading = false
      })
    },
    onClick(e) {
      this.coords = e.get('coords');
      console.log(this.coords)
    }
  },
  mounted() {
    this.defineMyPosition()
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