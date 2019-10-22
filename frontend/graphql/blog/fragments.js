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
