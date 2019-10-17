import graphene
from backend.blog.models import BlogPage
from backend.blog.schema.types import ArticleNode


# noinspection PyMethodMayBeStatic
class Query(graphene.ObjectType):
    articles = graphene.List(ArticleNode)
    article = graphene.Field(
        ArticleNode,
        slug=graphene.String(required=True),
    )

    def resolve_articles(self, info):
        return BlogPage.objects.live()[:12]

    def resolve_article(self, info, slug):
        # TODO: добавить редиректы на статьи, чей слаг был изменен
        return BlogPage.objects.get(slug=slug)
