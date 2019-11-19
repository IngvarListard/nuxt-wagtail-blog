<template>
  <!--  <v-footer color="#A9B9B9" app absolute padless>-->
  <!--    <v-card>-->
  <!--      <v-spacer />-->
  <!--      <v-btn text>Главная</v-btn>-->
  <!--      <v-btn text>Поиск</v-btn>-->
  <!--      <v-btn text>Настройки</v-btn>-->
  <!--      <v-spacer />-->
  <!--    </v-card>-->
  <!--    <v-divider></v-divider>-->
  <!--    <v-card>-->

  <!--      <v-row justify="center">-->
  <!--        <v-spacer />-->
  <!--        <v-spacer />-->
  <!--      </v-row>-->

  <!--    </v-card>-->
  <!--  </v-footer>-->
  <v-footer color="#A9B9B9" padless app absolute>
    <v-row justify="center" no-gutters>
      <v-btn
        depressed
        color="#313131"
        style="color: white;"
        href="https://github.com/JuniorsJourney"
        class="mx-3 my-2"
      >
        <v-icon color="white" class="mr-2">mdi-github-face</v-icon> GitHub
      </v-btn>
      <v-btn
        depressed
        color="#4A76A8"
        style="color: white;"
        href="https://github.com/JuniorsJourney"
        class="mx-3 my-2"
      >
        <v-icon color="white" class="mr-2">mdi-vk</v-icon> Вконтакте
      </v-btn>
      <v-btn
        depressed
        color="#2B9FD1"
        style="color: white;"
        href="https://github.com/JuniorsJourney"
        class="mx-3 my-2"
      >
        <v-icon color="white" class="mr-2">mdi-telegram</v-icon> Telegram
      </v-btn>
      <v-col class="py-4 text-center white--text" cols="12">
        {{ new Date().getFullYear() }} — <strong>Junior's Journey</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      links: ['Главная', 'О блоге']
    }
  }
}
</script>

<style scoped></style>
