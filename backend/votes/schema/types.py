from graphene_django import DjangoObjectType

from backend.votes.models import Vote


class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
