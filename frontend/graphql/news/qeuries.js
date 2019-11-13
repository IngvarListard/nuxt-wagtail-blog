import gql from 'graphql-tag'

const GET_NEWS_PAGE = gql`
  query($page: Int!, $pageSize: Int!, $search: String) {
    newsPage(page: $page, pageSize: $pageSize, search: $search)
  }
`

export { GET_NEWS_PAGE }
