import graphene
import requests


class Query(graphene.ObjectType):
    get_events_paged = graphene.Field(graphene.String)

    def resolve_get_events_paged(self, info):
        req = requests.get('https://api.dobrf.ru/events/?is_start_soon=true&ordering=-start_date')
        return req.content.decode('utf8')
