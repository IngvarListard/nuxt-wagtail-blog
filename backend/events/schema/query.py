import graphene
import requests
import json

from backend.events.models import Event
from backend.events.schema.types import EventType
from backend.events.services.map_services import GetNameCityByCoord, GetIdCityByName, GetEventIdsByLocation, \
    GetEventDataByEventId, GetEventDataByEventIds


class Query(graphene.ObjectType):
    get_events_paged = graphene.Field(graphene.String)
    get_events_by_position = graphene.List(EventType, x=graphene.Float(), y=graphene.Float())

    def resolve_get_events_paged(self, info):
        req = requests.get('https://api.dobrf.ru/events/?is_start_soon=true&ordering=-start_date')
        return req.content.decode('utf8')

    def resolve_get_events_by_position(self, info, x, y):
        events = Event.objects.annotate_distance_to_point(x, y).filter(distance__lt=0.5)


        # city_name = GetNameCityByCoord(x, y).execute()
        # city_id = GetIdCityByName(city_name).execute()
        # event_ids = GetEventIdsByLocation(city_id).execute()
        # event_data = GetEventDataByEventIds(event_ids).execute()
        # print(event_data)
        return events
