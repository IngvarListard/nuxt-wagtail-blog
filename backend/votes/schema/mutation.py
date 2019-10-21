import graphene

from backend.votes.service import VoteArticle


class Vote(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        article_id = graphene.ID()
        action = graphene.String()

    def mutate(self, info, **kwargs):
        # TODO
        return Vote(success=VoteArticle(user_id=1, **kwargs).execute())


class Mutation(graphene.ObjectType):
    vote = Vote.Field()
