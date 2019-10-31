from django.contrib.contenttypes.models import ContentType
from django.db.models import Count, Q, Case, When, Value as V, CharField

from backend.comments.models import Comment
from backend.core.service import Service
from backend.votes.models import Vote


class CommentCreation(Service):
    """Создание комментария"""
    def __init__(
        self,
        model_name: str,
        instance_id: int,
        text: str,
        user_id: int,
        parent_id: int = None,
    ):
        """
        :param model_name: Приложение и модель, к которой относится данный комментарий, разделенные точкой.
        :param instance_id: Запись в моделе, к которой относится данный комментарий.
        :param text: Текст комментария
        """
        assert text, 'Отсутствует текст комментария'
        assert '.' in model_name, 'Некорректное имя модели'
        self.model_name = model_name
        self.instance_id = instance_id
        self.text = text
        self.user_id = user_id
        self.parent_id = parent_id

    def execute(self):
        app_label, model = self.model_name.lower().split('.')
        content_type = ContentType(app_label=app_label, model=model)
        content_object = content_type.get_object_for_this_type(id=self.instance_id)
        return Comment.objects.create(
            content_object=content_object,
            user_id=self.user_id,
            text=self.text,
            parent_id=self.parent_id
        )


class GetComments(Service):

    def __init__(self, instance_id: int, model_name: str, user_id: int):
        self.instance_id = instance_id
        self.app, self.model = model_name.lower().split('.')
        self.user_id = user_id

    def execute(self):
        return (
            Comment.objects
                .filter(object_id=self.instance_id,
                        content_type__app_label=self.app,
                        content_type__model=self.model,
                        parent__isnull=True)
                .annotate(child_count=Count('children'),
                          likes=Count('votes__vote', filter=Q(votes__vote=Vote.LIKE)),
                          dislikes=Count('votes__vote', filter=Q(votes__vote=Vote.DISLIKE)))
                .annotate(user_vote=Case(
                    When(Q(votes__vote=Vote.LIKE) & Q(votes__user_id=self.user_id), then=V('like')),
                    When(Q(votes__vote=Vote.DISLIKE) & Q(votes__user_id=self.user_id), then=V('dislike')),
                    output_field=CharField(),
                    default=None
                ))
        )
