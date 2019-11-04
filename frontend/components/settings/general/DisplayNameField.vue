<template>
  <v-list-item>
    <v-list-item-action class="custom-list-action font-weight-bold"
      >ОТОБРАЖАЕМОЕ ИМЯ</v-list-item-action
    >
    <v-list-item-content>
      <span v-if="!edit">{{ user.displayName }}</span>
      <v-text-field
        v-else
        v-model="innerUser.displayName"
        outlined
        solo
        flat
        hide-details
        class="mt-3"
      />
    </v-list-item-content>
    <v-list-item-action>
      <v-btn v-if="!edit" icon @click="edit = true">
        <v-icon>mdi-pencil</v-icon>
      </v-btn>
      <v-btn v-else icon :loading="options.loading > 0" @click="save">
        <v-icon>mdi-check</v-icon>
      </v-btn>
    </v-list-item-action>
  </v-list-item>
</template>

<script>
import _ from 'lodash'
import { CURRENT_USER_CLIENT } from '../../../graphql/users/queries'
import settingsMixin from './general-settings-mixin'

export default {
  name: 'DisplayNameField',
  mixins: [settingsMixin],
  data() {
    return {
      user: {},
      innerUser: {},
      options: { loading: 0 },
      edit: false
    }
  },
  apollo: {
    user: CURRENT_USER_CLIENT
  },
  watch: {
    user: {
      handler(newVal) {
        this.innerUser = _.cloneDeep(newVal)
      },
      deep: true
    }
  },
  methods: {
    save() {
      this.saveUser({
        ...this.innerUser,
        options: this.options
      }).then(() => {
        this.edit = false
      })
    }
  }
}
</script>

<style scoped></style>
