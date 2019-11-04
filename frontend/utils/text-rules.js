export default {
  methods: {
    lettersOnly(text) {
      const re = /\d/
      return !re.test(text) || 'Только буквы'
    },
    validateEmail(text) {
      const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return re.test(String(text).toLowerCase()) || 'Невалидный email'
    }
  }
}
