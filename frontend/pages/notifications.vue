<template>
  <div>
    <v-card flat>
      <v-card-title>
        <v-tabs v-model="tabs" fixed-tabs>
          <v-tab>Публикации</v-tab>
          <v-tab>Подписки</v-tab>
          <v-tab>Упоминания</v-tab>
          <v-tab>События</v-tab>
        </v-tabs>
      </v-card-title>
    </v-card>
    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <publications />
      </v-tab-item>
      <v-tab-item> </v-tab-item>
      <v-tab-item> </v-tab-item>
      <v-tab-item> </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import Publications from '../components/notifications/notifications-center/Publications'
export default {
  name: 'Notifications',
  components: { Publications },
  data() {
    return {
      tabs: 0
    }
  }
}
</script>

<style scoped></style>
