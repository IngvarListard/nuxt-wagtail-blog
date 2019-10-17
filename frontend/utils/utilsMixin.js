const utilsMixin = {
  methods: {
    resolveUrl(url) {
      // TODO
      if (process.client) {
        console.log(this)
        console.log(process)
      }
      return 'http://localhost:8000' + url
    },
    resolveArticleImage(article) {
      return article.headImage
        ? this.resolveUrl(article.headImage.rendition.url)
        : require('@/assets/Real-Python-Video-Tutorials_Watermarked.webp')
    }
  }
}

export default utilsMixin
