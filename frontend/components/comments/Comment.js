export default {
  name: 'Comment',
  props: {
    text: String,
  },
  data() {
    return {
      patterns: [{ find: '\n', replace: '<br />' }]
    }
  },
  render(createElement) {
    return createElement('div', {
      domProps: {
        innerHTML: this.formatComment(this.text)
      }
    })
  },
  methods: {
    formatComment(text) {
      this.patterns.forEach(({ find, replace }) => {
        text = this.replaceAll(text, find, replace)
      })
      return text
    },

    replaceAll(str, find, replace) {
      return str.replace(new RegExp(find, 'g'), replace)
    }
  }
}
