<template>
  <div>
    <div id="button_vk"></div>
  </div>
</template>

<script>
export default {
  name: 'ReportToVk',
  props: {
    link: {
      type: String,
      default: ''
    },
    text: {
      type: String,
      default: 'Поделиться'
    }
  },
  data() {
    return {
      iconLink:' https://pp.userapi.com/c637418/v637418161/3a20c/aRLj3ll2fx4.jpg'
    }
  },
  mounted() {
    const head = document.getElementsByTagName('head')[0]
    const script = document.createElement('script')
    script.setAttribute('type', 'text/javascript')
    script.setAttribute('src', 'https://vk.com/js/api/share.js?95')
    script.setAttribute('charset', 'windows-1251')
    head.appendChild(script)

    setTimeout(() => {
      const url = this.link || this.$router.url
      document.getElementById('button_vk').innerHTML = VK.Share.button(url, {
        type: 'custom',
        text: `<img src="${this.iconLink}" width="64" height="64" />`
      })
    }, 1000)
  }
}
</script>

<style scoped></style>
