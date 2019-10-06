import { createUploadLink } from 'apollo-upload-client'
import { opts } from './build-http-link'

const uploadLink = createUploadLink(opts)
export { uploadLink }
