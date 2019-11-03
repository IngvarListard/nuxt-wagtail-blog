export default ctx => {
  ctx.app.apolloProvider.defaultClient.writeData({
    data: {
      errors: [],
      // getCurrentUser: {
      //   id: null,
      //   firstName: null,
      //   lastName: null,
      //   loggedIn: false,
      //   email: null,
      //   isActive: false,
      //   avatar: null,
      //   __typename: 'UserType'
      // }
    }
  })
}
