from django.db import models
from backend.users.models import User


class Notification(models.Model):
    COMMON = 'N'
    SUCCESS = 'S'
    WARNING = 'W'
    CRITICAL = 'C'
    TYPES = (COMMON, SUCCESS, WARNING, CRITICAL)
    NOTIFICATIONS_TYPE = (
        (COMMON, 'Уведомление'),
        (SUCCESS, 'Успешное'),
        (WARNING, 'Предупреждение'),
        (CRITICAL, 'Критическое'),
    )
    purpose = models.ForeignKey(
        User,
        related_name='notification_purpose_user',
        verbose_name='Цель',
        on_delete=models.PROTECT
    )
    created = models.ForeignKey(
        User,
        related_name='notification_created_user',
        verbose_name='Создатель',
        on_delete=models.PROTECT
    )
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    text = models.TextField('Текст уведомления')
    confirmed = models.BooleanField('Подтверждено', default=False)
    type = models.CharField(
        'Тип',
        max_length=1,
        choices=NOTIFICATIONS_TYPE,
        default='N'
    )
    link = models.CharField('Ссылка', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        default_permissions = ()

    def __str__(self):
        return str(self.id)
