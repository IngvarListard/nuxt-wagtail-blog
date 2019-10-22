const utilsMixin = {
  methods: {
    resolveUrl(url) {
      // TODO
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
