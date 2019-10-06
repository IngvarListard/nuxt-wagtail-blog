// https://vue-apollo.netlify.com/guide/apollo/subscriptions.html#setup
import { WebSocketLink } from 'apollo-link-ws'
import { httpLink } from './build-http-link'

const production = process.env.NODE_ENV === 'production'
let uri = 'ws://localhost:8000/ws/api_v1/'
let credentials = 'include'
if (production && process.client) {
  uri = `ws://${window.location.hostname}:${window.location.port}/ws/api_v1/`
  credentials = 'same-origin'
}

let link = httpLink
if (process.client) {
  link = new WebSocketLink({
    uri,
    credentials,
    options: {
      reconnect: true,
      credentials
    }
  })
}
const wsLink = link
export { wsLink }
