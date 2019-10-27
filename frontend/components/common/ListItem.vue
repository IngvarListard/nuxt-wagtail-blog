<template>
  <v-list-item :to="noAction ? undefined : btn.route" nuxt>
    <slot name="action">
      <v-list-item-action v-if="btn.icon">
        <v-icon>
          {{ btn.icon }}
        </v-icon>
      </v-list-item-action>
    </slot>
    <slot name="content">
      <v-list-item-content>
        <v-list-item-title>
          {{ btn.name }}
        </v-list-item-title>
      </v-list-item-content>
    </slot>
  </v-list-item>
</template>

<script>
export default {
  name: 'ListItem',
  props: {
    btn: {
      type: Object,
      default: () => ({})
    },
    noAction: Boolean
  }
}
</script>

<style scoped></style>
