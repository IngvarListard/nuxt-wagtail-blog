<template>
  <v-card outlined>
    <v-tabs v-model="tabs" centered grow background-color="#90A4AE" dark>
      <v-tabs-slider />
      <v-tab href="#best">Лучшее</v-tab>
      <v-tab href="#last">Последние</v-tab>
      <v-tab href="#tags">Тэги</v-tab>
    </v-tabs>
    <v-card-text>
      <v-tabs-items v-model="tabs">
        <v-tab-item value="best">
          <div v-for="(a, i) of 5" :key="i" class="d-flex flex-no-wrap justify-space-between">
            <v-avatar tile size="100" class="my-auto">
              <v-img max-width="250px" aspect-ratio="1" :src="require('@/assets/whereis1.png')" />
            </v-avatar>
            <div>
              <v-card-title class="headline" v-text="'Wagtail and Azure Storage Blob Containers'" />
              <v-card-text class="py-0">ДЕК. 11, 2019</v-card-text>
            </div>
          </div>
        </v-tab-item>
        <v-tab-item value="last">
          <div v-for="(a, i) of 5" :key="i" class="d-flex flex-no-wrap justify-space-between my-2">
            <v-avatar tile size="100" class="my-auto">
              <v-img max-width="250px" aspect-ratio="1" :src="require('@/assets/whereis1.png')" />
            </v-avatar>
            <div>
              <v-card-title class="headline" v-text="'Wagtail and Azure Storage Blob Containers'" />
              <v-card-text class="py-0">ДЕК. 11, 2019</v-card-text>
            </div>
          </div>
        </v-tab-item>
        <v-tab-item value="tags">
          tags
        </v-tab-item>
      </v-tabs-items>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'BestWidget',
  data() {
    return {
      tabs: 'best'
    }
  }
}
</script>

<style scoped></style>
