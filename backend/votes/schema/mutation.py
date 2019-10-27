import graphene

from backend.blog.service import CountArticleVotes
from backend.votes.schema.types import VotesCount
from backend.votes.service import VoteArticle


# noinspection PyMethodMayBeStatic
class Vote(graphene.Mutation):
    votes_count = graphene.Field(VotesCount)

    class Arguments:
        article_id = graphene.ID()
        action = graphene.String()

    def mutate(self, info, **kwargs):
        voter = VoteArticle(user_id=info.context.user.id, **kwargs)
        voter.execute()

        votes_counter = CountArticleVotes(info.context.user.id, voter.article.votes)
        votes_count = votes_counter.execute()
        votes_count['id'] = f'article_{kwargs["article_id"]}'
        return Vote(votes_count=votes_count)


class Mutation(graphene.ObjectType):
    vote = Vote.Field()
