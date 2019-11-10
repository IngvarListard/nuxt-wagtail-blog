<template>
  <div>
    <v-card flat>
      <v-card-title>
        <v-tabs v-model="tabs" fixed-tabs>
          <v-tab>Уведомления</v-tab>
        </v-tabs>
      </v-card-title>
    </v-card>
    <v-tabs-items v-model="tabs">
      <v-tab-item>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'Notifications',
  data() {
    return {
      tabs: 0
    }
  }
}
</script>

<style scoped></style>
