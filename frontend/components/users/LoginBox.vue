<template>
  <v-flex xs12 sm8 md4>
    <v-form ref="form" v-model="valid" @submit.prevent="submit">
      <v-card class="elevation-12">
        <v-toolbar dark color="primary">
          <v-toolbar-title>Авторизация</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-text-field
            v-model="login"
            prepend-icon="person"
            name="login"
            label="Логин"
            type="text"
            :rules="loginRules"
            @blur="clearLogin"
          ></v-text-field>
          <v-text-field
            id="password"
            v-model="password"
            prepend-icon="lock"
            name="password"
            label="Пароль"
            :rules="passRules"
            type="password"
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" type="submit">Войти</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-flex>
</template>
<script>
import { mapState } from 'vuex'

export default {
  name: 'LoginBox',
  data() {
    return {
      login: '',
      password: '',
      valid: false,
      loading: false,
      requestFail: false,
      loginRules: [
        v => !!v || 'Необходимо ввести логин',
        () => (this.requestFail ? 'Проверьте логин' : true)
      ],
      passRules: [
        v => !!v || 'Необходимо ввести пароль',
        () => (this.requestFail ? 'Проверьте пароль' : true)
      ]
    }
  },
  computed: {
    ...mapState({ user: state => state.auth.user })
  },
  methods: {
    async submit() {
      await this.$$auth.login({
        login: this.login,
        password: this.password
      })
      // await this.$store.dispatch('auth/login', {
      //   login: this.login,
      //   password: this.password
      // })
      // в компоненте Alarms ожидается что будет возвращен результат на событие 'loginSuccess'
      if (this.user.loggedIn) {
        this.requestFail = false
        this.$router.push({ name: 'index' })
      } else {
        this.requestFail = true
        this.$refs.form.validate()
      }
    },
    clearLogin() {
      let val = this.login
      if (/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,6})+$/.test(val)) {
        val = val.toLowerCase()
      }
      val = val.replace(/\s+/g, '')
      this.login = val
    }
  }
}
</script>
