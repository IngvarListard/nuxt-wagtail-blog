export default {
  name: 'TableOfContent',
  props: {
    depth: {
      type: [Number, String],
      default: 6
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
      let entry = `<li>${header.innerText}</li>`
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
