import graphene
from django.core.paginator import Paginator

from backend.notifications.models import Notification
from backend.notifications.schema.types import PagedNotificationsNode


# noinspection PyMethodMayBeStatic
class Query(graphene.ObjectType):
    notifications_page = graphene.Field(
        PagedNotificationsNode,
        **PagedNotificationsNode.pagination_kwargs,
    )

    def resolve_notifications_page(self, info, page, per_page):
        user = info.context.user
        all_notifications = Notification.objects.filter(purpose_id=user.id)
        pages = Paginator(all_notifications, per_page)
        notifications = pages.get_page(page)
        has_next = notifications.has_next()
        return PagedNotificationsNode(notifications=notifications, has_next=has_next)

