import { getMainDefinition } from 'apollo-utilities'

function generateUid() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    const r = (Math.random() * 16) | 0
    const v = c === 'x' ? r : (r & 0x3) | 0x8
    return v.toString(16)
  })
}
function isSubscription({ query }) {
  const definition = getMainDefinition(query)
  return (
    definition.kind === 'OperationDefinition' &&
    definition.operation === 'subscription' &&
    process.client
  )
}
function formatComment(text) {
  function replaceAll(str, find, replace) {
    return str.replace(new RegExp(find, 'g'), replace)
  }
  return replaceAll(text, '\n', '<br />')
}

export { generateUid, isSubscription, formatComment }
