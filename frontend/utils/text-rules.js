export default {
  methods: {
    lettersOnly(text) {
      const re = /\d/
      return !re.test(text) || 'Только буквы'
    }
  }
}
