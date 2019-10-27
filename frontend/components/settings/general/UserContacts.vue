<template>
  <settings-card>
    <template #title>
      Контактная информация
    </template>
    <template #body>
      <v-list-item @click="">
        <v-list-item-action class="custom-list-action font-weight-bold"
          >ЭЛЕКТРОННАЯ ПОЧТА</v-list-item-action
        >
        <v-list-item-content>
          project@example.com
        </v-list-item-content>
      </v-list-item>
      <v-divider />
      <v-list-item @click="">
        <v-list-item-action class="custom-list-action font-weight-bold"
          >СОЦИАЛЬНЫЕ СЕТИ</v-list-item-action
        >
        <v-list-item-content>
          vk.com
        </v-list-item-content>
      </v-list-item>
    </template>
  </settings-card>
</template>

<script>
import SettingsCard from './SettingsCard'
export default {
  name: 'UserContacts',
  components: { SettingsCard },
  props: {
    width: {
      type: [Number, String],
      default: undefined
    }
  }
}
</script>

<style scoped></style>
