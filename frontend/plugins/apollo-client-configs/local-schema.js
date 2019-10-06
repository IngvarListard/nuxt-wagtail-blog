import gql from 'graphql-tag'
const todoItemsQuery = gql`
  {
    todoItems @client {
      id
      text
      done
    }
  }
`
const typeDefs = gql`
  type Item {
    id: ID!
    text: String!
    done: Boolean!
  }

  type Mutation {
    checkItem(id: ID!): Boolean
    addItem(text: String!): Item
  }
`

const resolvers = {
  Mutation: {
    checkItem: (_, { id }, { cache }) => {
      const data = cache.readQuery({ query: todoItemsQuery })
      const currentItem = data.todoItems.find(item => item.id === id)
      currentItem.done = !currentItem.done
      cache.writeQuery({ query: todoItemsQuery, data })
      return currentItem.done
    }
  }
}

export { typeDefs, resolvers }
