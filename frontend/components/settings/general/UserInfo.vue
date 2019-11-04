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
        <birthday-field :user="user" />
        <v-divider />
        <password-field />
        <v-divider />
        <city-field />
        <v-divider />
        <v-list-item @click="">
          <v-list-item-action class="custom-list-action font-weight-bold"
            >ОТОБРАЖАЕМОЕ ИМЯ</v-list-item-action
          >
          <v-list-item-content>{{ user.displayName }}</v-list-item-content>
          <v-list-item-action>
            <v-btn icon>
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
      </v-list>
    </template>
  </settings-card>
</template>

<script>
import utilsMixin from '../../../utils/utilsMixin'
import { GET_CURRENT_USER } from '../../../graphql/users/queries'
import AvatarField from './AvatarField'
import NameField from './NameField'
import BirthdayField from './BirthdayField'
import PasswordField from './PasswordField'
import CityField from './CityField'
import SettingsCard from './SettingsCard'

export default {
  name: 'UserInfo',
  components: {
    SettingsCard,
    CityField,
    PasswordField,
    BirthdayField,
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
      query: GET_CURRENT_USER,
      update({ getCurrentUser }) {
        return getCurrentUser
      },
      prefetch: false
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
