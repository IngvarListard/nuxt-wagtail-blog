from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    time = models.DateTimeField('Дата', auto_now_add=True)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.DO_NOTHING,
        verbose_name='Пользователь',
        null=True,
        blank=True
    )
    text = models.TextField('Комментарий')
    is_system = models.BooleanField('Системный комментарий', default=False)
    parent = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name='Актуальный комментарий',
        symmetrical=False
    )


    # Создание комментария
    # current_user = info.context.user
    # app_label, model = comment_kind.lower().split('.')
    # content_type = ContentType(app_label=app_label, model=model)
    # content_object = content_type.get_object_for_this_type(id=object_id)
    # new_comment = Comment.objects.create(content_object=content_object, user=current_user, description=description)
    #
    # # Зачем?
    # if link and len(link) < 2:
    #     raise SngyException('Системная ошибка: передана неправильная ссылка для уведомлений пользователей.'
    #                         ' Комментарий создан, но уведомления не отправлены.')
    # new_comment.comment_notify(current_user.id, notify_users, link)
