<template>
  <v-card outlined>
    <v-toolbar flat>
      <v-avatar tile>
        <v-img :src="formatAvatarUrl(author.avatar)" />
      </v-avatar>
      <table style="width: 100%" class="text-center">
        <tr>
          <th style="color: mediumseagreen;">204,2</th>
          <th style="color: #5E88B0;">121</th>
          <th style="color: #5E88B0;">60</th>
        </tr>
        <tr class="text-center text--secondary" style="font-size: 14px;">
          <td>Карма</td>
          <td>Подписчики</td>
          <td>Подписки</td>
        </tr>
      </table>

      <v-spacer />
      <v-btn outlined color="primary" class="mr-2 hidden-sm-and-down"
        ><v-icon>mdi-email</v-icon> Написать</v-btn
      >
      <v-btn outlined color="success" class="hidden-sm-and-down"
        >Подписаться</v-btn
      >
    </v-toolbar>
    <v-card-text>
      <div class="text--primary">
        {{ `${author.firstName} ${author.lastName}` }}
        <span class="txt">{{ `@${author.displayName}` }}</span>
        <br />
        {{ author.bio }}
      </div>
    </v-card-text>
    <v-divider class="hidden-md-and-up" />
    <v-card-actions class="hidden-md-and-up justify-space-around">
      <v-btn outlined color="primary" class="mr-2">
        <v-icon>mdi-email</v-icon> Написать</v-btn
      >
      <v-btn outlined color="success">Подписаться</v-btn>
    </v-card-actions>
    <v-divider />
    <v-card-actions>
      <v-row dense class="text-center">
        <v-col class="txt">Facebook</v-col>
        <v-col class="txt">Twitter</v-col>
        <v-col class="txt">Telegram</v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<script>
import utilsMixin from '../../utils/utilsMixin'

export default {
  name: 'AuthorCard',
  mixins: [utilsMixin],
  props: {
    author: {
      type: Object,
      required: true,
      default: () => ({})
    }
  }
}
</script>

<style scoped>
.txt:hover {
  text-decoration: underline;
  cursor: pointer;
  color: #3676ab;
  word-wrap: break-word;
}
.txt {
  color: #619ccd;
  font-weight: normal;
  word-break: keep-all;
}
</style>
