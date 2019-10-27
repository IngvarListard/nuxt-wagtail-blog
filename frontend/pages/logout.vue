<script>
export default {
  name: 'Logout',
  functional: true,
  middleware({ store: { dispatch }, redirect }) {
    dispatch('auth/logout')
    redirect('/')
  },
  render() {
    return ''
  }
}
</script>
