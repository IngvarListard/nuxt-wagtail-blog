import graphene
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied

from backend.comments.models import Comment
from backend.comments.schema.types import CommentNode


# noinspection PyMethodMayBeStatic,PyIncorrectDocstring
class CreateComment(graphene.Mutation):
    comment = graphene.Field(CommentNode)

    class Arguments:
        comment_kind = graphene.String(required=True)
        object_id = graphene.Int(required=True)
        text = graphene.String(required=True)

    def mutate(self, info, comment_kind, object_id, text):
        """Создание комментария

        :param comment_kind: Приложение и модель, к которой относится данный комментарий, разделенные точкой.
        :param object_id: Запись в моделе, к которой относится данный комментарий.
        :param text: Текст комментария
        """
        current_user = info.context.user
        if not current_user.is_authenticated:
            raise PermissionDenied('Сначала необходимо осуществить вход')
        if not text:
            raise ValueError('Ошибка: введите текст комментария')
        if '.' not in comment_kind:
            raise ValueError('Ошибка: Неправильное имя объекта')

        app_label, model = comment_kind.lower().split('.')
        content_type = ContentType(app_label=app_label, model=model)
        content_object = content_type.get_object_for_this_type(id=object_id)
        new_comment = Comment(content_object=content_object, user=current_user, text=text)
        new_comment.save()

        return CreateComment(comment=new_comment)


class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()
