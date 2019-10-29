import graphene
from graphene_django import DjangoObjectType

from backend.votes.models import Vote


class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote


class VotesCountNode(graphene.ObjectType):
    id = graphene.ID(description='ID родителя')
    likes = graphene.Int(description='Количество лайков')
    dislikes = graphene.Int(description='Количество дизлайков')
    user_vote = graphene.String(description='Оценка пользователя')
