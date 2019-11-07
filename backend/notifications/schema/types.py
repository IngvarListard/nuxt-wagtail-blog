import graphene
import graphene_django

from backend.core.schema.types import PagedNode
from backend.notifications.models import Notification


class NotificationNode(graphene_django.DjangoObjectType):

    class Meta:
        model = Notification


class PagedNotificationsNode(PagedNode):
    notifications = graphene.List(NotificationNode)
