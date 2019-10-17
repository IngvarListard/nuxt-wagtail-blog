import gql from 'graphql-tag'

const GET_ARTICLE = gql`
  query($slug: String!) {
    article(slug: $slug) {
      id
      title
      headImage {
        id
        title
        file
        rendition(max: "750x400", format: "jpeg", bgcolor: "ffffff") {
          url
          width
          height
        }
        headerImg: rendition(fill: "1024x250-c75") {
          url
        }
        renditionList(sizes: [30, 60]) {
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
              url
              width
              height
            }
            headerImg: rendition(fill: "1024x250-c75") {
              url
            }
            renditionList(sizes: [30, 60]) {
              srcSet
            }
          }
        }
      }
    }
  }
`

const ARTICLE_FRAGMENT = gql`
  fragment ArticleContents on ArticleNode {
    id
    title
    headImage {
      id
      title
      file
      rendition(max: "750x400", format: "jpeg", bgcolor: "ffffff") {
        url
        width
        height
      }
      headerImg: rendition(fill: "1024x250-c75") {
        url
      }
      renditionList(sizes: [30, 60]) {
        srcSet
      }
    }
    date
    intro
    slug
  }
`

const GET_ARTICLES = gql`
  {
    articles {
      ...ArticleContents
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

export { GET_ARTICLE, GET_ARTICLES, GET_RANDOM_ARTICLE }
