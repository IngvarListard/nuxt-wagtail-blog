<template>
  <settings-card :title-class="['my-1', 'py-1']">
    <template #title>
      <v-row align="center" dense class="my-0 py-0">
        <div>Коротко о себе</div>
        <v-spacer />
        <v-list-item-action>
          <v-btn v-if="!edit" icon @click="edit = true">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn v-else icon :loading="options.loading > 0" @click="save">
            <v-icon>mdi-check</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-row>
    </template>
    <template #body>
      <v-card-text>
        <div v-if="!edit" class="text-primary">
          <comment :text="user.bio || 'Здесь пока ничего нет'" />
        </div>
        <v-textarea v-else v-model="innerUser.bio" outlined counter="500" />
      </v-card-text>
    </template>
  </settings-card>
</template>

<script>
import _ from 'lodash'
import Comment from '../../comments/Comment'
import SettingsCard from './SettingsCard'
import settingsMixin from './general-settings-mixin'
import { CURRENT_USER_CLIENT } from '../../../graphql/users/queries'

export default {
  name: 'Bio',
  components: { Comment, SettingsCard },
  mixins: [settingsMixin],
  data() {
    return {
      edit: false,
      innerUser: { bio: '' },
      options: { loading: 0 },
      user: {}
    }
  },
  apollo: {
    user: {
      query: CURRENT_USER_CLIENT
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
      }).then(() => {
        this.edit = false
      })
    }
  }
}
</script>

<style scoped></style>
