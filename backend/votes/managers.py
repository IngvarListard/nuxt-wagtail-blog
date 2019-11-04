from django.db import models
from django.db.models import Sum, Count, Q
from django.db.models.manager import BaseManager, QuerySet


class VoteQuerySet(QuerySet):
    def likes(self):
        # Забираем queryset с записями больше 0
        return self.filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.aggregate(Sum('vote')).get('vote__sum') or 0

    def votes_count(self) -> dict:
        from backend.votes.models import Vote
        return self.aggregate(
            likes=Count('pk', filter=Q(vote=Vote.LIKE)),
            dislikes=Count('pk', filter=Q(vote=Vote.DISLIKE)),
        )


class VoteManager(BaseManager.from_queryset(VoteQuerySet)):
    use_for_related_fields = True
