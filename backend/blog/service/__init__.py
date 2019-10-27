from backend.votes.managers import VoteManager
from backend.votes.models import Vote


class CountArticleVotes:

    def __init__(self, user_id: int, votes: VoteManager):
        self.votes = votes
        self.user_id = user_id

    def execute(self) -> dict:
        votes_count = self.votes.votes_count()
        vote = self.votes.filter(user_id=self.user_id)
        try:
            vote = self.votes.get(user_id=self.user_id)
        except Vote.DoesNotExist:
            votes_count['user_vote'] = None
        else:
            votes_count['user_vote'] = 'like' if vote.vote == Vote.LIKE else 'dislike'
            print(vote.vote)
            print(votes_count)

        return votes_count
