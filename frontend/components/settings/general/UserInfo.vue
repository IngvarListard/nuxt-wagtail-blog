<template>
  <settings-card>
    <template #title>
      Профиль
    </template>
    <template #subtitle>
      Некоторая информация может быть видна другим пользователям
    </template>
    <template #body>
      <v-list class="pb-0 mb-0">
        <avatar-field />
        <v-divider />
        <name-field />
        <v-divider />
        <birthday-field />
        <v-divider />
        <password-field />
        <v-divider />
        <city-field />
        <v-divider />
        <v-list-item @click="">
          <v-list-item-action class="custom-list-action font-weight-bold"
            >ОТОБРАЖАЕМОЕ ИМЯ</v-list-item-action
          >
          <v-list-item-content>##PuSSyDESTROYER$$</v-list-item-content>
        </v-list-item>
      </v-list>
    </template>
  </settings-card>
</template>

<script>
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
  props: {
    width: {
      type: [Number, String],
      default: 800
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
