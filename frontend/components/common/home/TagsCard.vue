<template>
  <v-card outlined>
    <v-card-title style="font-size: 23px" class="font-weight-light pt-2 px-3"
      >Тэги</v-card-title
    >
    <v-card-text class="px-3">
      <v-chip
        v-for="(c, i) of 25"
        :key="i"
        x-small
        label
        class="mx-1"
        color="#F6F6F6"
      >
        <strong style="color: gray">test_tag_{{ c }}</strong>
      </v-chip>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'TagsCard'
}
</script>

<style scoped></style>
