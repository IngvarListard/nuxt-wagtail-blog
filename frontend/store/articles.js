export const state = () => ({
  page: 1,
  perPage: 12,
  hasNext: true
})

export const mutations = {
  setPage(state, page) {
    state.page = page
  },
  setHasNext(state, hasNext) {
    state.hasNext = hasNext
  }
}

export const actions = {
}

export const getters = {
}
