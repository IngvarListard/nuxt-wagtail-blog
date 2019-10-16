<template>
  <v-row justify="center">
    <v-col sm="12" lg="10">
      <v-row justify="center">
        <v-col v-for="(c, i) of 13" :key="i" lg="4" md="6" sm="12">
          <div>
            <v-card flat>
              <v-img
                :src="
                  require('@/assets/Real-Python-Video-Tutorials_Watermarked.webp')
                "
              />
            </v-card>
            <v-card-title
              style="color: #619CCD; font-size: 22px;"
              class="px-0 pt-2"
            >
              <span class="txt"
                >Get Started With Django: Build a Portfolio App</span
              >
            </v-card-title>
            <v-card-text class="px-0">
              <v-icon small>mdi-calendar</v-icon>
              Окт. 15, 2019
              <v-icon small class="mb-1">mdi-tag-multiple</v-icon>
              <v-chip x-small label link class="mb-1">Спорт</v-chip>
              <v-chip x-small label link class="mb-1">Отдых</v-chip>
            </v-card-text>
          </div>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Feed'
}
</script>

<style scoped>
.txt:hover {
  text-decoration: underline;
  cursor: pointer;
  color: #3676ab;
}
</style>
