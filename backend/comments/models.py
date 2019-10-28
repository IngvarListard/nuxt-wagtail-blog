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
    changed = models.BooleanField('Изменено', default=False)
