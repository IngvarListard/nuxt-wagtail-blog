import graphene

from backend.blog.service import CountVotes
from django.core.exceptions import PermissionDenied
from backend.votes.schema.types import VotesCount
from backend.votes.service import ToVote


# noinspection PyMethodMayBeStatic
class Vote(graphene.Mutation):
    votes_count = graphene.Field(VotesCount)

    class Arguments:
        instance_id = graphene.ID()
        action = graphene.String()
        vote_to = graphene.String()

    def mutate(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            raise PermissionDenied('Сначала необходимо осуществить вход в систему')
        voter = ToVote(
            user_id=info.context.user.id,
            instance=kwargs['instance_id'],
            action=kwargs['action'],
            model_name=kwargs['vote_to']
        )
        voter.execute()

        votes_counter = CountVotes(info.context.user.id, voter.instance.votes)
        votes_count = votes_counter.execute()
        votes_count['id'] = f'__{kwargs["vote_to"]}_{kwargs["instance_id"]}'
        return Vote(votes_count=votes_count)


class Mutation(graphene.ObjectType):
    vote = Vote.Field()
