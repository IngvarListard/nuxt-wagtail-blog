<template>
  <settings-card>
    <template #title>
      Профиль
    </template>
    <template #subtitle>
      Некоторая информация может быть видна другим пользователям
    </template>
    <template #avatar>
      <v-row justify="center">
        <avatar-field :user="user" />
      </v-row>
    </template>
    <template #body>
      <v-list class="pb-0 mb-0">
        <v-divider />
        <name-field :user="user" />
        <v-divider />
        <display-name-field :user="user" />
      </v-list>
    </template>
  </settings-card>
</template>

<script>
import utilsMixin from '../../../utils/utilsMixin'
import { CURRENT_USER_CLIENT } from '../../../graphql/users/queries'
import AvatarField from './AvatarField'
import NameField from './NameField'
import SettingsCard from './SettingsCard'
import DisplayNameField from './DisplayNameField'

export default {
  name: 'UserInfo',
  components: {
    DisplayNameField,
    SettingsCard,
    NameField,
    AvatarField
  },
  mixins: [utilsMixin],
  props: {
    width: {
      type: [Number, String],
      default: 800
    }
  },
  data() {
    return {
      user: {}
    }
  },
  apollo: {
    user: {
      query: CURRENT_USER_CLIENT
    }
  }
}
</script>

<style>
.custom-list-action {
  min-width: 130px;
  font-size: 12px;
  color: gray;
}
</style>
