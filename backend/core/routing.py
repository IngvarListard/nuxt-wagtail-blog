from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

import backend.notifications.routing
import backend.core.consumers

# TODO: можно сделать коллектор как со схемой, вместо ручного добавления и импорта
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/api_v1/', backend.core.consumers.GraphqlWsConsumer),  # GraphQL подписки
        ])
    ),
})
