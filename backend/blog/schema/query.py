import graphene
from django.core.paginator import Paginator
from taggit.models import Tag

from backend.blog.models import BlogPage
from backend.blog.schema.types import ArticleNode, PagedArticlesNode
from backend.core.api.graphene_wagtail import TagNode


# noinspection PyMethodMayBeStatic
class Query(graphene.ObjectType):
    articles_page = graphene.Field(
        PagedArticlesNode,
        **PagedArticlesNode.pagination_kwargs
    )
    article = graphene.Field(
        ArticleNode,
        slug=graphene.String(required=True),
    )
    random_article = graphene.Field(ArticleNode)
    tags = graphene.List(TagNode)
    article_search = graphene.List(ArticleNode, search_line=graphene.String())

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

    def resolve_article_search(self, info, search_line):
        blog_pages = BlogPage.objects.all()
        if search_line:
            blog_pages = blog_pages.search(search_line)
        return blog_pages
