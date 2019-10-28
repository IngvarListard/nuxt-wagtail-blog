<template>
  <div>
    <v-tabs v-model="tabs">
      <v-tab>Публикации</v-tab>
      <v-tab>Комментарии</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <v-card outlined>
          <v-card-title>
            Статья
          </v-card-title>
          <v-card-text>
            Тело статьи
          </v-card-text>
        </v-card>
        <v-card outlined>
          <v-card-title>
            Статья
          </v-card-title>
          <v-card-text>
            Тело статьи
          </v-card-text>
        </v-card>
        <v-card outlined>
          <v-card-title>
            Статья
          </v-card-title>
          <v-card-text>
            Тело статьи
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card outlined>
          <v-card-title>comment</v-card-title>
          <v-card-text>comment body</v-card-text>
        </v-card>
        <v-card outlined>
          <v-card-title>comment</v-card-title>
          <v-card-text>comment body</v-card-text>
        </v-card>
        <v-card outlined>
          <v-card-title>comment</v-card-title>
          <v-card-text>comment body</v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'Bookmarks',
  layout: 'profile',
  data() {
    return {
      tabs: 0
    }
  }
}
</script>

<style scoped></style>
