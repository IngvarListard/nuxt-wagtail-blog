import moment from 'moment'

const production = process.env.NODE_ENV === 'production'
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
    formatAvatarUrl(url) {
      return url ? this.resolveUrl('/media/' + url) : ''
    },
    formatDate(date) {
      return moment(date).format('ll')
    },
    formatCommentDate(date) {
      return moment(date)
        .subtract(1, 'days')
        .calendar()
    },
    formatUrl(url) {
      if (!url) {
        return url
      }
      if (url[0] !== '/') {
        url = '/' + url
      }
      return (production ? '' : '//localhost:8000') + url
    }
  }
}

export default utilsMixin
