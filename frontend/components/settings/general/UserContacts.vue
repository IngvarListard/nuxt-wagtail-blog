<template>
  <settings-card>
    <template #title>
      Контактная информация
    </template>
    <template #body>
      <email-field />
    </template>
  </settings-card>
</template>

<script>
import SettingsCard from './SettingsCard'
import EmailField from './EmailField'
export default {
  name: 'UserContacts',
  components: { EmailField, SettingsCard },
  props: {
    width: {
      type: [Number, String],
      default: undefined
    }
  }
}
</script>

<style scoped></style>
