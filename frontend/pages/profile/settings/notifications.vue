<template>
  <v-row>
    <v-col cols="8">
      <v-simple-table>
        <thead>
          <tr>
            <th>
              <strong>Уведомления о новых публикациях в комментариях</strong>
            </th>
            <th>На сайте</th>
            <th>Почта</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Которые я написал</td>
            <td>
              <v-checkbox class="ma-auto" hide-details></v-checkbox>
            </td>
            <td>
              <v-checkbox class="ma-auto" hide-details></v-checkbox>
            </td>
          </tr>
          <tr>
            <td>В которых я оставил комментарий</td>
            <td>
              <v-checkbox class="ma-auto" hide-details></v-checkbox>
            </td>
            <td>
              <v-checkbox class="ma-auto" hide-details></v-checkbox>
            </td>
          </tr>
          <tr>
            <td>Которые добавил в закладки</td>
            <td>
              <v-checkbox class="ma-auto" hide-details></v-checkbox>
            </td>
            <td>
              <v-checkbox class="ma-auto" hide-details></v-checkbox>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
      <v-card flat class="my-2">
        <v-card-title>Отправлять мне письма</v-card-title>
        <v-divider />
        <v-card-text>
          <v-checkbox
            hide-details
            class="shrink"
            label="Об изменениях на сайте"
          />
          <v-checkbox
            hide-details
            class="shrink"
            label="О новых для меня возможностях на сайте"
          />
          <v-checkbox
            hide-details
            class="shrink"
            label="О новых сообщениях в диалогах"
          />
          <v-checkbox
            hide-details
            class="shrink"
            label="О новых ответах на мои комментарии"
          />
          <v-checkbox
            hide-details
            class="shrink"
            label="При упоминании меня в публикациях или в комментариях"
          />
          <v-checkbox
            hide-details
            class="shrink"
            label="При добавлении нового подписчика"
          />
        </v-card-text>
      </v-card>

      <v-card flat class="my-2">
        <v-card-title
          >Выберите частоту рассылки дайджеста о самом интересном по
          вашим</v-card-title
        >
        <v-divider />
        <v-card-text>
          <v-row class="mx-2">
            <v-checkbox
              v-model="mailing"
              hide-details
              class="shrink"
              label="Присылать дайджест на почту"
            />
            <v-spacer />
            <v-select
              v-model="item"
              :items="items"
              item-value="value"
              item-text="name"
              style="max-width: 150px;"
              :disabled="!mailing"
            />
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Notifications',
  layout: 'profile',
  data() {
    return {
      item: 0,
      items: [
        { value: 0, name: 'Раз в день' },
        { value: 1, name: 'Раз в неделю' },
        { value: 2, name: 'Раз в месяц' }
      ],
      mailing: false
    }
  }
}
</script>

<style scoped></style>
