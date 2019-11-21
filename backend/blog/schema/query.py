import graphene
from django.core.paginator import Paginator
from django.db.models import Sum, F, Value as V
from django.db.models.functions import Coalesce
from taggit.models import Tag

from backend.blog.models import BlogPage, BlogPageTag
from backend.blog.schema.types import ArticleNode, PagedArticlesNode, PagedBlogPageTagNode
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
    article_search = graphene.Field(
        PagedArticlesNode,
        search_line=graphene.String(),
        tags=graphene.List(graphene.String),
        sort_by=graphene.String(),
        order=graphene.String(),
        **PagedArticlesNode.pagination_kwargs
    )
    tags_page = graphene.Field(
        PagedBlogPageTagNode,
        search=graphene.String(),
        tags_list=graphene.List(graphene.String),
        **PagedBlogPageTagNode.pagination_kwargs
    )

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

    def resolve_article_search(self, info, search_line, page, per_page, **filters):
        # TODO: вынести в сервис
        tags = filters.get('tags') or []
        blog_pages = BlogPage.objects.all()
        sort_map = {
            'rating': '',
            'viewed': '',
            'date': '',
        }
        if search_line:
            blog_pages = blog_pages.search(search_line).get_queryset()
        if tags:
            blog_pages = blog_pages.filter(tags__name__in=tags).distinct()
        if filters.get('sort_by'):
            sort = F(filters.get('sort_by', 'rating'))
            sort = getattr(sort, filters.get('order', 'desc'))()
            blog_pages = blog_pages.annotate(
                rating=Coalesce(Sum('votes__vote'), 0)
            ).order_by(sort)
        pages = Paginator(blog_pages, per_page)
        articles = pages.get_page(page)
        has_next = articles.has_next()
        return PagedArticlesNode(articles=articles, has_next=has_next)

    def resolve_tags_page(self, info, page, per_page, search='', tags_list=None):
        tags_list = tags_list or list()
        tags = BlogPageTag.objects.all()
        if search:
            tags = tags.filter(tag__name__contains=search)
        if tags_list:
            tags = tags.filter(tag__name__in=tags_list)
        pages = Paginator(tags, per_page)
        tags_page = pages.get_page(page)
        has_next = tags_page.has_next()
        return PagedBlogPageTagNode(tags=tags_page, has_next=has_next)
