from backend.votes.managers import VoteManager
from backend.votes.models import Vote


class CountArticleVotes:

    def __init__(self, user_id: int, votes: VoteManager):
        self.votes = votes
        self.user_id = user_id

    def execute(self) -> dict:
        votes_count = self.votes.votes_count()
        vote = self.votes.filter(user_id=self.user_id)
        votes_count['user_vote'] = None
        if vote:
            votes_count['user_vote'] = 'like' if vote.first().vote == Vote.LIKE else 'dislike'

        return votes_count
