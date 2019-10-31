import moment from 'moment'
moment.locale('ru-ru')
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
    },
    formatDate(date) {
      return moment(date).format('ll')
    },
    formatCommentDate(date) {
      return moment(date)
        .subtract(1, 'days')
        .calendar()
    }
  }
}

export default utilsMixin
