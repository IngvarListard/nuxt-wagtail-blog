<template>
  <v-card flat class="pa-0">
    <pre
      :class="languageClass"
      class="ma-0"
    ><code style="box-shadow: none;" v-html="renderedCode"></code></pre>
  </v-card>
</template>

<script>
export default {
  name: 'CodeBlock',
  props: {
    code: {
      type: String,
      default: ''
    },
    language: {
      type: String,
      default: 'markup'
    }
  },
  computed: {
    languageClass() {
      return `language-${this.language}`
    },
    renderedCode() {
      const Prism = require('prismjs')
      return Prism.highlight(this.code, Prism.languages[this.language])
    }
  },
  mounted() {
    const Prism = require('prismjs')
    Prism.highlightAll()
  }
}
</script>

<style scoped></style>
