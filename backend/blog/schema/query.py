import graphene
from django.core.paginator import Paginator
from taggit.models import Tag

from backend.blog.models import BlogPage
from backend.blog.schema.types import ArticleNode, PagedArticlesNode
from backend.core.api.graphene_wagtail import TagNode


# noinspection PyMethodMayBeStatic
class Query(graphene.ObjectType):
    # articles = graphene.List(
    #     ArticleNode,
    #     skip=graphene.Int(required=True, description='Пагинация. Сколько объектов пропустить от начала'),
    #     first=graphene.Int(required=True, description='Пагинация. Количество объектов на странице'),
    # )
    articles_page = graphene.Field(
        PagedArticlesNode,
        page=graphene.Int(required=True, description='Номер страницы'),
        per_page=graphene.Int(required=True, description='Количество элеменов на странице'),
    )
    article = graphene.Field(
        ArticleNode,
        slug=graphene.String(required=True),
    )
    random_article = graphene.Field(ArticleNode)
    tags = graphene.List(TagNode)

    # def resolve_articles(self, info, skip, first):
    #     return BlogPage.objects.live()[skip:][:first]
    #
    def resolve_articles_page(self, info, page, per_page):
        pages = Paginator(BlogPage.objects.live(), per_page)
        articles = pages.get_page(page)
        has_next = articles.has_next()
        return PagedArticlesNode(articles=articles, has_next=has_next)

    def resolve_article(self, info, slug):
        # TODO: добавить редиректы на статьи, чей слаг был изменен
        return BlogPage.objects.get(slug=slug)

    def resolve_random_article(self, info):
        return BlogPage.objects.live().order_by('?').first()

    def resolve_tags(self, info):
        return Tag.objects.all()[:10]
