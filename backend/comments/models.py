from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from backend.votes.models import Vote


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
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        verbose_name='Первый в обсуждении',
        related_name='children',
        on_delete=models.CASCADE
    )
    changed = models.BooleanField('Изменено', default=False)
    votes = GenericRelation(Vote, related_query_name='comments')
    deleted = models.BooleanField('Удалено', default=False)
