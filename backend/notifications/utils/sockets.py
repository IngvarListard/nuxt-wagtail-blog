from typing import Iterable, Union

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from backend.notifications.models import Notification
from backend.users.models import User


# noinspection PyShadowingBuiltins
def send_notifications(users: Iterable[Union[User, str, int]],
                       message: str,
                       type: str = None,
                       link: str = None):
    assert type in (*Notification.TYPES, None), 'Неверный тип уведомления'
    users_ids = list(map(lambda u: int(u.id) if isinstance(u, User) else int(u), users))
    notifications = []
    for user_id in users_ids:
        notifications.append(Notification(
            purpose_id=user_id,
            created_id=user_id,
            text=message,
            type=type,
            link=link,
        ))
    Notification.objects.bulk_create(notifications)

    channel_layer = get_channel_layer()
    for notification in notifications:
        async_to_sync(channel_layer.group_send)(
            'user{}_group'.format(notification.purpose_id),
            {
                'type': 'notification',
                'notification': {
                    'text': notification.text,
                    'id': notification.id,
                    'date': str(notification.date),
                    'type': notification.type,
                    'link': notification.link,
                    'action': 'addPopup',
                    'namespace': 'notifications'
                }},
        )
