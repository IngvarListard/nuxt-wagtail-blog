import channels_graphql_ws
import graphene

from backend.notifications.schema.types import NotificationNode


class Notifications(channels_graphql_ws.Subscription):
    notification = graphene.Field(NotificationNode)

    @staticmethod
    def subscribe(root, info):
        user_id = info.context.user.id
        return [f'user{user_id}_notifications']

    @staticmethod
    def publish(notification, info):
        return Notifications(notification=notification)

    @staticmethod
    def get_user_group(user_id: int) -> str:
        return f'user{user_id}_notifications'


class Subscription(graphene.ObjectType):
    notifications = Notifications.Field()
