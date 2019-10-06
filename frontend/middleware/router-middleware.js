export default ctx => {
  const toPath = ctx.route.path
  if (toPath === '/admin' || toPath === '/admin/') {
    if (process.env.NODE_ENV === 'development')
      ctx.redirect('localhost:8000/admin')
  }
}
