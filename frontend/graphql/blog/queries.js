import gql from 'graphql-tag'
import { ARTICLE_FRAGMENT } from './fragments'

const GET_ARTICLE = gql`
  query($slug: String!) {
    article(slug: $slug) {
      id
      title
      views
      votesCount {
        id
        likes
        dislikes
        userVote
      }
      tags {
        id
        name
        slug
      }
      headImage {
        id
        title
        file
        rendition(max: "750x400", format: "jpeg", bgcolor: "ffffff") {
          id
          url
          width
          height
        }
        headerImg: rendition(fill: "1024x250-c75") {
          id
          url
        }
        renditionList(sizes: [30, 60]) {
          renditionList {
            id
            url
          }
          srcSet
        }
      }
      date
      intro
      slug
      body {
        ... on CodeBlock {
          value
          blockType
        }
        ... on ParagraphBlock {
          value
          blockType
        }
        ... on HeadingBlock {
          value
          blockType
        }
        ... on MarkdownBlock {
          value
          blockType
        }
        ... on ImageBlock {
          blockType
          image {
            id
            title
            file
            rendition(max: "750x400", format: "jpeg", bgcolor: "ffffff") {
              id
              url
              width
              height
            }
            headerImg: rendition(fill: "1024x250-c75") {
              id
              url
            }
            renditionList(sizes: [30, 60]) {
              renditionList {
                id
              }
              srcSet
            }
          }
        }
      }
    }
  }
`

const GET_PAGED_ARTICLES = gql`
  query($page: Int!, $perPage: Int!) {
    articlesPage(page: $page, perPage: $perPage) {
      hasNext
      articles {
        ...ArticleContents
      }
    }
  }
  ${ARTICLE_FRAGMENT}
`

const GET_RANDOM_ARTICLE = gql`
  {
    randomArticle {
      ...ArticleContents
    }
  }
  ${ARTICLE_FRAGMENT}
`

const TAGS = gql`
  {
    tags {
      id
      name
      slug
    }
  }
`

// const GET_ARTICLE_FRAGMENT = gql``

export { GET_ARTICLE, GET_RANDOM_ARTICLE, TAGS, GET_PAGED_ARTICLES }
