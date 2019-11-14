import graphene
import requests
import json

from backend.events.services.map_services import GetNameCityByCoord, GetIdCityByName, GetEventIdsByLocation, \
    GetEventDataByEventId, GetEventDataByEventIds


class Query(graphene.ObjectType):
    get_events_paged = graphene.Field(graphene.String)
    get_events_by_position = graphene.Field(graphene.String, x=graphene.Float(), y=graphene.Float())

    def resolve_get_events_paged(self, info):
        req = requests.get('https://api.dobrf.ru/events/?is_start_soon=true&ordering=-start_date')
        return req.content.decode('utf8')

    def resolve_get_events_by_position(self, info, x, y):
        city_name = GetNameCityByCoord(x, y).execute()
        city_id = GetIdCityByName(city_name).execute()
        event_ids = GetEventIdsByLocation(city_id).execute()
        event_data = GetEventDataByEventIds(event_ids).execute()
        print(event_data)
        return json.dumps(event_data)
