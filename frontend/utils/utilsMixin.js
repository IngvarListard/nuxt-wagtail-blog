const utilsMixin = {
  methods: {
    resolveUrl(url) {
      // TODO
      return 'http://localhost:8000' + url
    },
    resolveArticleImage(article) {
      // Вместо пустой строки можно вставить изображение-заглушку, но работает это не очень красиво
      return article.headImage
        ? this.resolveUrl(article.headImage.rendition.url)
        : ''
    }
  }
}

export default utilsMixin
