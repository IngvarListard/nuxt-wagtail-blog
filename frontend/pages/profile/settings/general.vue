<template>
  <v-row justify="center">
    <div>
      <div style="text-align: center;" class="display-1">
        Личные данные
      </div>
      <div style="text-align: center; color: #5b5b5b;" class="subtitle-1">
        Основная информация
      </div>
    </div>
    <v-col cols="12">
      <user-info class="col-12" />
    </v-col>
    <v-col cols="12">
      <bio />
    </v-col>
    <v-col cols="12">
      <user-contacts />
    </v-col>
  </v-row>
</template>

<script>
import UserInfo from '../../../components/settings/general/UserInfo'
import UserContacts from '../../../components/settings/general/UserContacts'
import Bio from '../../../components/settings/general/Bio'

export default {
  name: 'General',
  components: { Bio, UserContacts, UserInfo },
  layout: 'profile',
  computed: {
    width() {
      if (this.$vuetify.breakpoint.lg) {
        return '800'
      } else if (this.$vuetify.breakpoint.md) {
        return 800
      }
      return null
    }
  }
}
</script>

<style scoped></style>
