export default ctx => {
  const toPath = ctx.route.path
  const settingsRegex = /\/settings\//g
  if (toPath === '/admin' || toPath === '/admin/') {
    if (process.env.NODE_ENV === 'development')
      ctx.redirect('localhost:8000/admin')
  } else if (settingsRegex.test(toPath)) {
    if (!ctx.store.state.auth.user.loggedIn) ctx.redirect('/login')
  }
}
