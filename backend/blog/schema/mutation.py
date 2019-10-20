import graphene

from backend.blog.models import BlogPage


class IncrementArticleViews(graphene.Mutation):
    result = graphene.Boolean()

    class Arguments:
        slug = graphene.String(required=True)

    # noinspection PyMethodMayBeStatic
    def mutate(self, info, slug):
        article = BlogPage.objects.get(slug=slug)
        article.views += 1
        article.save()
        return IncrementArticleViews(result=True)


class Mutation(graphene.ObjectType):
    increment_article_views = IncrementArticleViews.Field()
