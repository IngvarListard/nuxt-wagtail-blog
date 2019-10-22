import gql from 'graphql-tag'

const ARTICLE_FRAGMENT = gql`
  fragment ArticleContents on ArticleNode {
    id
    title
    views
    votesCount {
      id
      likes
      dislikes
      userVote
      __typename
    }
    tags {
      id
      name
      slug
      __typename
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
        __typename
      }
      headerImg: rendition(fill: "1024x250-c75") {
        id
        url
        __typename
      }
      renditionList(sizes: [30, 60]) {
        renditionList {
          id
          url
          __typename
        }
        srcSet
        __typename
      }
    }
    date
    intro
    slug
    __typename
  }
`

const ARTICLE_VOTES_FRAGMENT = gql`
  fragment ArticleVotes on ArticleNode {
    id
    votesCount {
      id
      likes
      dislikes
      userVote
    }
  }
`

export { ARTICLE_FRAGMENT, ARTICLE_VOTES_FRAGMENT }
