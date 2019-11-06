import graphene_django

from backend.notifications.models import Notification


class NotificationNode(graphene_django.DjangoObjectType):

    class Meta:
        model = Notification
