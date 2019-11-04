from django.db.models import QuerySet
from django.utils.functional import cached_property

from backend.votes.managers import VoteManager, VoteQuerySet
from backend.votes.models import Vote


class CountVotes:

    def __init__(self, user_id: int, model_name: str, instance_id: int):
        self.user_id = user_id
        self.app, self.model = model_name.lower().split('.')
        self.instance_id = instance_id

    @cached_property
    def votes(self) -> VoteQuerySet:
        return Vote.objects.filter(
            content_type__app_label=self.app,
            content_type__model=self.model,
            object_id=self.instance_id,
        )

    def execute(self) -> dict:
        votes_count = self.votes.votes_count()
        vote = self.votes.filter(user_id=self.user_id)
        try:
            vote = self.votes.get(user_id=self.user_id)
        except Vote.DoesNotExist:
            votes_count['user_vote'] = None
        else:
            votes_count['user_vote'] = 'like' if vote.vote == Vote.LIKE else 'dislike'

        return votes_count
