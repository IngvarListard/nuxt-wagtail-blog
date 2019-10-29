import graphene
from graphene_django import DjangoObjectType

from backend.blog.service import CountVotes
from backend.comments.models import Comment
from backend.core.utils import id_generator
from backend.votes.schema.types import VotesCountNode


class CommentNode(DjangoObjectType):
    child_count = graphene.Int()
    votes_count = graphene.Field(VotesCountNode)

    def resolve_votes_count(self, info):
        votes_counter = CountVotes(info.context.user.id, self.votes)
        votes_count = votes_counter.execute()
        votes_count_node = VotesCountNode(**votes_count)
        votes_count_node.id = id_generator(self, 'blog.BlogPage', self.id)
        return votes_count_node

    class Meta:
        model = Comment


class PagedCommentsNode(graphene.ObjectType):
    id = graphene.ID(description='Сгенерированный ID')
    comments = graphene.List(CommentNode, description='Комментарии')
    total_count = graphene.Int(description='Общее количество комментариев')


@id_generator.register(VotesCountNode)
@id_generator.register(PagedCommentsNode)
def paged_comments_node_id_generator(instance, parent_model_name: str, parent_model_id: int):
    return f'__{type(instance)}_{parent_model_name}_{parent_model_id}'
