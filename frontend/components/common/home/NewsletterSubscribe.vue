<template>
  <v-card color="#F47555" dark outlined class="">
    <v-card-title class="font-weight-bold text-uppercase mx-auto">
      <div class="text-center mx-auto" style="word-break: keep-all; font-size: 22px;">
        Подписка на рассылку
      </div></v-card-title
    >
    <v-card-text
      style="font-size: 18px; text-align: center; line-height: 1.3; color: white;"
    >
      Подписывайтесь на обновления и получайте уведомления о новых интересных
      статьях по почте.
      <v-text-field filled label="Введите Ваш email:" dark class="mt-3" />
      <v-btn x-large class="text-uppercase" dark block color="white" outlined
        >Подписаться!</v-btn
      >
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'NewsletterSubscribe'
}
</script>

<style scoped></style>
