import graphene
import requests

NEWS_URL = 'https://api.dobrf.ru/open-api/v1/news/'


class Query(graphene.ObjectType):
    news_page = graphene.JSONString(
        page=graphene.Int(required=True),
        page_size=graphene.Int(required=True),
        search=graphene.String()
    )

    def resolve_news_page(self, info, **params):
        r = requests.get(NEWS_URL, params=params)
        return r.json()
