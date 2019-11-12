export default {
  name: 'TableOfContent',
  props: {
    depth: {
      type: [Number, String],
      default: 6
    }
  },
  // mounted() {
  //   const headersIds = new Array(
  //     ...document.getElementById('article').querySelectorAll('h1, h2')
  //   ).map(header => header.id)
  //   headersIds.forEach(id => {
  //     document.querySelectorAll(`a[id='#${id}']`).forEach(el => {
  //       el.addEventListener('click', this.scrollTo(id))
  //     })
  //   })
  // },
  methods: {
    scrollTo(id) {
      const vuetify = this.$vuetify
      return function() {
        return vuetify.goTo(id)
      }
    }
  },
  render(createElement) {
    if (process.server) return ''
    const headers = document
      .getElementById('article')
      .querySelectorAll('h1, h2, h3, h4, h5, h6')
    let toc = ''
    let level = 0
    headers.forEach((header, i, arr) => {
      const regExp = /[\d]/
      const currentLevel = parseInt(header.localName.match(regExp)[0])
      if (currentLevel > parseInt(this.depth)) return
      const slug = header.innerText.split(' ').join('-')
      header.id = slug
      // let entry = `<li><a>${header.innerText}</a></li>`
      let entry = `<li><a href="#${slug}">${header.innerText}</a></li>`
      if (currentLevel < level) {
        entry = '</ul>'.repeat(level - currentLevel) + entry
      } else if (currentLevel > level) {
        entry = '<ul>'.repeat(currentLevel - level) + entry
      }
      toc += entry
      level = currentLevel
    })
    return createElement('div', {
      domProps: {
        innerHTML: toc
      }
    })
  }
}
