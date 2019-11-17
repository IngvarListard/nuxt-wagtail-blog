from graphene_django import DjangoObjectType

from backend.events.models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
