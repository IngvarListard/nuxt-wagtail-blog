const utilsMixin = {
  methods: {
    resolveUrl(url) {
      if (process.client) {
        console.log(this)
        console.log(process)
      }
      return 'http://localhost:8000' + url
    }
  }
}

export default utilsMixin
