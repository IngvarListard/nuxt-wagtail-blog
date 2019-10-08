import graphene
from backend.blog.models import BlogPage
from backend.blog.schema.types import ArticleNode


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleNode)
    article = graphene.Field(
        ArticleNode,
        article_id=graphene.ID(required=True)
    )

    @graphene.resolve_only_args
    def resolve_articles(self):
        return BlogPage.objects.live()

    def resolve_article(self, info, article_id):
        return BlogPage.objects.get(id=article_id)
