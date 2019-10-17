import gql from 'graphql-tag'

const GET_ARTICLE = gql`
  query($articleId: ID!) {
    article(articleId: $articleId) {
      id
      title
      date
      intro
      body {
        ... on CodeBlock {
          value
        }
        ... on ParagraphBlock {
          value
        }
        ... on HeadingBlock {
          value
        }
        ... on RecipeBlock {
          recipe {
            title
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
            ingredients {
              ... on IngredientBlock {
                value
                name
                quantity
                unit
              }
            }
            instructions
          }
        }
      }
    }
  }
`

export { GET_ARTICLE }
