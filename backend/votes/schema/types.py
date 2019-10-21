import graphene
from graphene_django import DjangoObjectType

from backend.votes.models import Vote


class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote


class VotesCount(graphene.ObjectType):
    likes = graphene.Int(description='Количество лайков')
    dislikes = graphene.Int(description='Количество дизлайков')
    user_vote = graphene.String(description='Оценка пользователя')
