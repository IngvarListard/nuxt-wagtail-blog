<template>
  <v-card outlined>
    <v-card-text>
      <v-row align="center" class="text--primary px-1" dense>
        Поделиться публикацией
        <v-spacer />
        <v-btn fab small elevation="0" color="#40AEEF" class="mr-1">
          <v-icon color="white">mdi-twitter</v-icon>
        </v-btn>
        <v-btn fab small elevation="0" color="#4A739A" class="mr-1">
          <v-icon color="white">mdi-vk</v-icon>
        </v-btn>
        <v-btn fab small elevation="0" color="#009FDA" class="mr-1">
          <v-icon color="white">mdi-telegram</v-icon>
        </v-btn>
        <v-btn fab small elevation="0" color="#3A5A9A" class="mr-1">
          <v-icon color="white">mdi-facebook</v-icon>
        </v-btn>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'ShareCard'
}
</script>

<style scoped></style>
