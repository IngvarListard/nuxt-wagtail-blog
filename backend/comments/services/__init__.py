from django.contrib.contenttypes.models import ContentType

from backend.comments.models import Comment
from backend.core.service import Service


class CommentCreation(Service):
    """Создание комментария"""
    def __init__(
        self,
        model_name: str,
        instance_id: int,
        text: str,
        user_id: int
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

    def execute(self):
        app_label, model = self.model_name.lower().split('.')
        content_type = ContentType(app_label=app_label, model=model)
        content_object = content_type.get_object_for_this_type(id=self.instance_id)
        return Comment.objects.create(
            content_object=content_object,
            user_id=self.user_id,
            text=self.text
        )
