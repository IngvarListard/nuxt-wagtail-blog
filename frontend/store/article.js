export const state = () => ({
  article: {
    id: null
  }
})

export const mutations = {
  setCurrentArticle({ article }, { id }) {
    article.id = id
  }
}
