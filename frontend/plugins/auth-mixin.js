import Vue from 'vue'
import { mapActions } from 'vuex'

Vue.mixin({
  computed: {
    $$user() {
      return this.$store.state.auth.user
    },
    $$auth() {
      return {
        hasPerm: this.$store.getters['auth/hasPerm'],
        // ...mapActions('auth', [
        //   'login',
        //   'logout',
        //   'register',
        //   'changePassword'
        // ]),
        login: ({ login, password }) =>
          this.$store.dispatch('auth/login', { login, password }),
        logout: () => this.$store.dispatch('auth/logout')
      }
    }
  }
})
