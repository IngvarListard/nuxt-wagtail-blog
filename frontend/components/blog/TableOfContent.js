export default {
  name: 'TableOfContent',
  props: {
    depth: {
      type: [Number, String],
      default: 6
    },
    fontSize: {
      type: [Number, String],
      default: 14
    }
  },
  mounted() {
    const headersIds = new Array(
      ...document.getElementById('article').querySelectorAll(this.depthStr)
    ).map(header => header.id)
    headersIds.forEach(id => {
      document.querySelectorAll(`span[id='#${id}']`).forEach(el => {
        el.addEventListener('click', this.scrollTo(id))
      })
    })
  },
  computed: {
    depthStr() {
      let depth = ''
      for (let i = 0; i < parseInt(this.depth); i++) {
        if (depth.length === 0) {
          depth += `h${i + 1}`
          continue
        }
        depth += `, h${i + 1}`
      }
      return depth
    }
  },
  methods: {
    scrollTo(id) {
      const vuetify = this.$vuetify
      return function() {
        return vuetify.goTo('#' + id)
      }
    }
  },
  render(createElement) {
    if (process.server) return ''
    const headers = document
      .getElementById('article')
      .querySelectorAll(this.depthStr)
    let toc = ''
    let level = 0
    headers.forEach((header, i, arr) => {
      const regExp = /[\d]/
      const currentLevel = parseInt(header.localName.match(regExp)[0])
      const slug = header.innerText.split(' ').join('-')
      header.id = slug
      let entry = `
      <li style="font-size: ${this.fontSize}px;">
        <span class="toc-link" id="#${slug}">${header.innerText}</span>
      </li>
      `
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
