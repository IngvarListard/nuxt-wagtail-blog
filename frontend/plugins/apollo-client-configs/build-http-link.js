import { BatchHttpLink } from 'apollo-link-batch-http'
import { HttpLink } from 'apollo-link-http'

const production = process.env.NODE_ENV === 'production'
// Настраиваем соединение в зависимости от среды
// Для разработки необходимо указывать credentials: include так как порты серверов разные
let credentials = 'include'
// Для разработки используем локальный сервер на другом порту
let path = 'http://localhost:8000/api_v1'
if (production && process.client) {
  credentials = 'same-origin'
  path = '/api_v1' // если будут ошибки здесь, надо указать полный путь
} else if (production && process.server) {
  path = 'http://backend:8000/api_v1'
}
const uri = path

const opts = {
  credentials,
  uri
}
/*
 ** Для продакшена используем накопление запросов в один (batching) с макс. интервалом ожидания 50 мс
 ** https://www.apollographql.com/docs/link/links/batch-http.html
 */
if (production) {
  opts.batchInterval = 50
}
const httpLink = production ? new BatchHttpLink(opts) : new HttpLink(opts)

export { httpLink, opts, uri }
