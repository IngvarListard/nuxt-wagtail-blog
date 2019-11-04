export default ctx => {
  const path = ctx.route.path
  const re = /\/settings\//g
  if (re.test(path)) {
    if (!ctx.store.auth.state.user.loggedIn) {
      ctx.redirect('/login')
    }
  }
}
