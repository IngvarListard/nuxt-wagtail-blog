export const state = () => ({
  skip: 0,
  first: 12
})

export const mutations = {
  increaseSkip(state, amount) {
    state.skip += amount
    console.log('INCREASED', amount, state.skip)
  }
}

export const actions = {
}

export const getters = {
}
