<template>
  <div style="max-width: 350px;">
    <v-row :justify="justify">
      <v-hover #default="{ hover }">
        <v-card outlined @click="edit = !edit">
          <v-avatar class="profile" color="grey" size="164" tile>
            <v-img :src="formatAvatarUrl(user.avatar)">
              <v-row justify="center" align="end">
                <v-expand-transition>
                  <v-btn
                    v-if="hover"
                    depressed
                    small
                    tile
                    color="primary"
                    class="transition-fast-in-fast-out"
                    width="100%"
                    @click.self.exact="edit = !edit"
                    >Обновить</v-btn
                  >
                </v-expand-transition>
              </v-row>
            </v-img>
          </v-avatar>
        </v-card>
      </v-hover>
    </v-row>
    <v-row :justify="justify" dense>
      <v-expand-transition>
        <v-file-input
          v-if="edit"
          v-model="newAvatar"
          label="Выберите файл"
          outlined
          style="width: 250px;"
          solo
          flat
          class="my-2 pa-0"
          prepend-icon=""
          append-icon="mdi-camera"
          hide-details
        />
      </v-expand-transition>
    </v-row>
    <v-row dense justify="center">
      <v-expand-transition>
        <v-btn
          v-if="newAvatar && edit"
          color="success"
          depressed
          @click="sendAvatar"
        >
          Отправить
        </v-btn>
      </v-expand-transition>
    </v-row>
  </div>
</template>

<script>
import { UPDATE_AVATAR } from '../../../graphql/users/mutations'
import utilsMixin from '../../../utils/utilsMixin'

export default {
  name: 'AvatarField',
  mixins: [utilsMixin],
  props: {
    justify: {
      type: String,
      default: 'center'
    },
    user: {
      type: Object,
      default: () => ({
        id: null,
        url: null
      })
    }
  },
  data() {
    return {
      edit: false,
      newAvatar: null
    }
  },
  methods: {
    sendAvatar() {
      this.$apollo
        .mutate({
          mutation: UPDATE_AVATAR,
          variables: {
            userId: this.$$user.id,
            file: this.newAvatar
          },
          context: { hasUpload: true }
        })
        .then(() => {
          this.newAvatar = null
          this.edit = false
        })
        .catch(e => {
          this.newAvatar = null
          throw new Error(e)
        })
    }
  }
}
</script>

<style scoped></style>
