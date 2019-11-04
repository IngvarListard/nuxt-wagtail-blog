<template>
  <v-form v-model="valid">
    <v-dialog v-model="options.dialog" width="500">
      <v-card>
        <v-card-title>Изменение имени</v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="12" lg="6" md="12" sm="12">
              <v-text-field
                v-model="innerUser.firstName"
                label="Имя"
                :rules="[lettersOnly]"
                outlined
                solo
                counter="25"
                flat
              />
            </v-col>
            <v-col cols="12" lg="6" md="12" sm="12">
              <v-text-field
                v-model="innerUser.lastName"
                label="Фамилия"
                :rules="[lettersOnly]"
                outlined
                solo
                counter="30"
                flat
              />
            </v-col>
          </v-row>
        </v-card-text>
        <v-divider />
        <v-card-actions>
          <v-spacer />
          <v-btn outlined color="error" @click="options.dialog = false"
            >Отмена</v-btn
          >
          <v-btn text color="success" :disabled="!valid" @click="save"
            >Сохранить</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-list-item>
      <v-list-item-action class="custom-list-action font-weight-bold"
        >ИМЯ</v-list-item-action
      >
      <v-list-item-content>{{
        `${user.firstName || $$user.firstName} ${user.lastName ||
          $$user.lastName}`
      }}</v-list-item-content>
      <v-list-item-action>
        <v-btn
          icon
          :loading="options.loading > 0"
          @click="options.dialog = true"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </v-list-item-action>
    </v-list-item>
  </v-form>
</template>

<script>
import _ from 'lodash'
import textRules from '../../../utils/text-rules'
import settingsMixin from './general-settings-mixin'

export default {
  name: 'NameField',
  mixins: [textRules, settingsMixin],
  props: {
    user: {
      type: Object,
      default: () => ({
        id: null,
        firstName: '',
        lastName: ''
      })
    }
  },
  data() {
    return {
      dialog: false,
      valid: true,
      loading: 0,
      options: {
        dialog: false,
        loading: 0
      },
      innerUser: {
        id: null,
        firstName: '',
        lastName: ''
      }
    }
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
      })
    }
  }
}
</script>

<style scoped></style>
