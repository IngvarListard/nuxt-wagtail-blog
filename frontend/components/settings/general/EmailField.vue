<template>
  <v-form v-model="valid">
    <v-list-item>
      <v-list-item-action
        v-if="!($vuetify.breakpoint.name === 'xs' && edit)"
        class="custom-list-action font-weight-bold"
        >ЭЛЕКТРОННАЯ ПОЧТА</v-list-item-action
      >
      <v-list-item-content>
        <span v-if="!edit">{{ user.email || 'Не указана' }}</span>
        <v-text-field
          v-else
          v-model="innerUser.email"
          outlined
          flat
          solo
          label="Электронная почта"
          class="mt-7 mb-0"
          :rules="[validateEmail]"
        />
      </v-list-item-content>
      <v-list-item-action>
        <v-btn v-if="!edit" icon @click="edit = true">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn
          v-else
          icon
          :loading="options.loading > 0"
          :disabled="!valid"
          @click="save"
        >
          <v-icon>mdi-check</v-icon>
        </v-btn>
      </v-list-item-action>
    </v-list-item>
  </v-form>
</template>

<script>
import _ from 'lodash'
import { CURRENT_USER_CLIENT } from '../../../graphql/users/queries'
import { UPDATE_USER_EMAIL } from '../../../graphql/users/mutations'
import textRules from '../../../utils/text-rules'

export default {
  name: 'EmailField',
  mixins: [textRules],
  data() {
    return {
      user: {},
      innerUser: {},
      options: { loading: 0 },
      edit: false,
      valid: true
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
      this.$apollo
        .mutate({
          mutation: UPDATE_USER_EMAIL,
          variables: {
            id: this.innerUser.id,
            email: this.innerUser.email
          }
        })
        .then(() => {
          this.edit = false
        })
        .catch(e => {
          this.edit = false
          throw new Error(e)
        })
    }
  }
}
</script>

<style scoped></style>
