from graphene_django import DjangoObjectType

from backend.blog.models import BlogPage


class ArticleNode(DjangoObjectType):
    class Meta:
        model = BlogPage
        only_fields = ['id', 'title', 'date', 'intro', 'body']


