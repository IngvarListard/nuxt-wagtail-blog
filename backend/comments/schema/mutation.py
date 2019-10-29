import graphene
from django.core.exceptions import PermissionDenied

from backend.comments.schema.types import CommentNode
from backend.comments.services import CommentCreation


# noinspection PyMethodMayBeStatic,PyIncorrectDocstring
class CreateComment(graphene.Mutation):
    comment = graphene.Field(CommentNode)

    class Arguments:
        model_name = graphene.String(required=True)
        instance_id = graphene.ID(required=True)
        text = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        current_user = info.context.user
        if not current_user.is_authenticated:
            raise PermissionDenied('Сначала необходимо осуществить вход')
        comment_creation = CommentCreation(user_id=current_user.id, **kwargs)
        new_comment = comment_creation.execute()
        return CreateComment(comment=new_comment)


class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()
