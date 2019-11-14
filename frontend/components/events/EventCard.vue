<template>
  <div>
    <v-card flat @click="openEvent(activity)">
      <v-img
        :src="
          activity.image
            ? activity.image.original
            : require('@/assets/plug.jpg')
        "
        aspect-ratio="1.8"
      />
    </v-card>
    <v-card-title :style="{ 'font-size': titleSize }" class="px-0 pb-1 pt-2">
      <slot name="title">
        <span
          style="color: #619CCD;"
          class="txt"
          @click="openEvent(activity)"
          >{{ activity.name }}</span
        >
      </slot>
    </v-card-title>
    <v-icon>mdi-calendar</v-icon>
    <span
      class="font-weight-regular"
      style="font-size: 16px; color: #999999;"
      >{{ formatDate(activity.start_date) }}</span
    >
  </div>
</template>

<script>
import utilsMixin from '../../utils/utilsMixin'
export default {
  name: 'EventCard',
  mixins: [utilsMixin],
  props: {
    activity: {
      type: Object,
      default: () => ({
        id: null,
        name: null,
        image: null,
        start_date: null
      })
    },
    titleSize: {
      type: String,
      default: '22px'
    }
  },
  methods: {
    openEvent(event) {
      let url =
        'https://добровольцыроссии.рф/organizations/1?event=' + event.slug
      window.open(url, '_blank')
    }
  }
}
</script>

<style scoped>
.txt:hover {
  text-decoration: underline;
  cursor: pointer;
  color: #3676ab;
  word-wrap: break-word;
}
.txt {
  color: #619ccd;
  font-weight: normal;
  word-break: keep-all;
}
a {
  text-decoration: none !important;
}
</style>
