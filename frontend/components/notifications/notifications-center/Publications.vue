<template>
  <v-data-table :headers="headers" :items="items" item-key="id" hide-default-footer />
</template>

<script>
export default {
  name: 'Publications',
  data() {
    return {
      headers: [
        { text: 'Автор', value: 'author', align: 'left', width: '120px' },
        {
          text: 'Заголовок',
          value: 'title',
          align: 'left'
        },
        {
          text: 'Комментарии',
          value: 'comments',
          width: '150px',
          align: 'left'
        }
      ],
      items: [
        {
          id: 1,
          author: '@aureliano',
          title: 'Результаты народного голосования',
          comments: 23
        },
        {
          id: 2,
          author: '@buendia',
          title: 'Подведение итогов собрания',
          comments: 14
        }
      ]
    }
  }
}
</script>

<style scoped></style>
