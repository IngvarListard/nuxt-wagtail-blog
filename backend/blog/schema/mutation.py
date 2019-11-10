import graphene

from backend.blog.models import BlogPage
from backend.blog.schema.types import ArticleNode


class IncrementArticleViews(graphene.Mutation):
    article = graphene.Field(ArticleNode)

    class Arguments:
        slug = graphene.String(required=True)

    # noinspection PyMethodMayBeStatic
    def mutate(self, info, slug):
        article = BlogPage.objects.get(slug=slug)
        article.views += 1
        article.save()
        return IncrementArticleViews(article=article)


class Mutation(graphene.ObjectType):
    increment_article_views = IncrementArticleViews.Field()
