<template>
  <div>
    <v-snackbar
      v-for="(item, index) in errors"
      :key="index"
      v-model="item.show"
      :timeout="0"
      multi-line
      top
      color="error"
    >
      {{ item.text }}
      <v-btn text icon @click.native="hideError(item.id)">
        <v-icon color="white">close</v-icon>
      </v-btn>
    </v-snackbar>
    <v-dialog v-model="dialog" persistent max-width="30%">
      <login-box @loginSuccess="loginDialog = false" />
    </v-dialog>
  </div>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex'
import LoginBox from '@/components/users/LoginBox'

export default {
  name: 'Errors',
  components: { LoginBox },
  data() {
    return {
      loginDialog: false,
      show: true
    }
  },
  computed: {
    dialog() {
      return this.loginDialog && this.$route.name !== 'login'
    },
    ...mapGetters({ errors: 'errorsGetter' })
  },
  methods: {
    push(text) {
      if (text === '') {
        return
      }
      if (text.indexOf('matching query does not exist') > 0) {
        this.$router.replace({ name: 'page404' })
        return
      }
      if (text.indexOf('::') > -1) {
        const split = text.split('::', 2)
        text = split[1] || ''
        const code = parseInt(split[0])
        if (
          code === 401 &&
          this.$router.currentRoute.name &&
          this.$router.currentRoute.name !== 'login'
        ) {
          // Необходим логин
          this.loginDialog = true
          return
        }
        if (this.$router.currentRoute.path === '/') {
          return
        }
      }
      const length = this.errors.length
      const last = length > 0 ? this.errors[length - 1] : null
      if (last && last.message === text && last.show) {
        return
      }
      const newError = {
        message: text,
        show: false
      }
      this.errors.push(newError)
      if (this.errors.length > 5) {
        this.errors.shift()
      }
      setTimeout(() => {
        this.errors[this.errors.length - 1].show = true
      }, 50)
    },
    ...mapMutations({
      removeError: 'removeError',
      hideError: 'hideError'
    })
  }
}
</script>
