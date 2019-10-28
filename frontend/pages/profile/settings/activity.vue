<template>
  <div>
    <v-tabs v-model="tabs">
      <v-tab>Публикации</v-tab>
      <v-tab>Комментарии</v-tab>
      <v-tab>Упоминания</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <v-card>
          <v-card-title>Публикация1</v-card-title>
          <v-card-text>Текст публикации, лайкосики</v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card>
          <v-card-title>Комментарий1</v-card-title>
          <v-card-text>Текст комментария, публикация, лайкосики</v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card>
          <v-card-title>Упоминания</v-card-title>
          <v-card-text>Текст упоминания, публикация</v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'Activity',
  layout: 'profile',
  data() {
    return {
      tabs: 0
    }
  }
}
</script>

<style scoped></style>
