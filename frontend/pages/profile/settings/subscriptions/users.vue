<template>
  <div>
    <v-row justify="center">
      <v-col lg="8" md="8" sm="12" cols="12">
        <div class="d-flex my-auto display-1">Пользователи</div>
        <v-text-field
          v-model="searchField"
          height="52"
          outlined
          placeholder="Найти компанию"
          append-icon="mdi-magnify"
          class="pt-2"
        />
        <v-data-table :headers="headers" :items="items" :search="searchField">
        </v-data-table>
      </v-col>
      <v-col lg="4" md="4" sm="12" cols="12">
        <v-card outlined>
          <v-card-title>Фильтры</v-card-title>
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam
            aut corporis dicta eaque eum facilis, iure natus nesciunt nisi nobis
            odio quae quibusdam quos rerum sed, ut veritatis voluptatem.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Users',
  layout: 'profile',
  data() {
    return {
      searchField: '',
      headers: [
        { text: 'Название', value: 'name', align: 'left' },
        {
          text: 'Подписчики',
          value: 'subscribers',
          width: '120px',
          align: 'center'
        },
        { text: 'Рейтинг', value: 'rating', width: '120px', align: 'center' }
      ],
      items: [
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 },
        { name: 'Lorem', rating: 555, subscribers: 350 }
      ]
    }
  }
}
</script>

<style scoped></style>
