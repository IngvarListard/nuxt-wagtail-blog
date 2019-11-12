<template>
  <v-card outlined>
    <v-card-title class="py-3 font-weight-regular"
      >На этой странице</v-card-title
    >
    <v-card-text>
      <client-only>
        <table-of-content :depth="depth" :font-size="fontSize" />
      </client-only>
    </v-card-text>
  </v-card>
</template>

<script>
import TableOfContent from './TableOfContent'
export default {
  name: 'TocCard',
  components: { TableOfContent },
  props: {
    depth: {
      type: [String, Number],
      default: 2
    },
    fontSize: {
      type: [Number, String],
      default: 16
    }
  }
}
</script>

<style>
.toc-link:hover {
  text-decoration: underline;
  cursor: pointer;
  color: #3676ab;
  word-wrap: break-word;
}
.toc-link {
  color: #619ccd;
  font-weight: normal;
  word-break: keep-all;
}
a.toc-link {
  text-decoration: none !important;
}
</style>
