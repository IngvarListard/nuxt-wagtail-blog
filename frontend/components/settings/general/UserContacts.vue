<template>
  <settings-card>
    <template #title>
      Контактная информация
    </template>
    <template #body>
      <email-field />
      <v-divider />
      <v-list-item @click="">
        <v-list-item-action class="custom-list-action font-weight-bold"
          >СОЦИАЛЬНЫЕ СЕТИ</v-list-item-action
        >
        <v-list-item-content>
          vk.com
        </v-list-item-content>
        <v-list-item-action>
          <v-btn icon>
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </template>
  </settings-card>
</template>

<script>
import SettingsCard from './SettingsCard'
import EmailField from "./EmailField";
export default {
  name: 'UserContacts',
  components: {EmailField, SettingsCard },
  props: {
    width: {
      type: [Number, String],
      default: undefined
    }
  }
}
</script>

<style scoped></style>
