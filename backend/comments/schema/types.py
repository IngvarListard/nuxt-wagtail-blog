from graphene_django import DjangoObjectType

from backend.comments.models import Comment


class CommentNode(DjangoObjectType):

    class Meta:
        model = Comment
