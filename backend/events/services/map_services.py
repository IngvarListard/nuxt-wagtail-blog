import requests
import json
from threading import Thread


class GetIdCityByName:
    def __init__(self, name):
        self.name = name
        self.url = 'https://api.dobrf.ru/open-api/v1/regions/?search={}'.format(name)

    def execute(self):
        response = requests.get(self.url)
        response_data = json.loads(response.content.decode('utf-8'))
        return response_data[0]['id']


class GetNameCityByCoord:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.point = '{},{}'.format(self.y, self.x)
        self.api_key = 'a0fd0f38-a513-489e-a35f-a3dda7e3cdb6'
        self.url = 'https://geocode-maps.yandex.ru/1.x/?apikey={}&format=json&kind=locality&geocode={}'.format(self.api_key, self.point)

    def execute(self) -> str:
        response = requests.get(self.url)
        response_data = json.loads(response.content.decode('utf-8'))
        city = response_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
        return city


class GetCoordByAddress:
    def __init__(self, address):
        self.address = address
        self.api_key = 'a0fd0f38-a513-489e-a35f-a3dda7e3cdb6'
        self.url = 'https://geocode-maps.yandex.ru/1.x/?apikey={}&format=json&kind=locality&geocode={}'.format(self.api_key, self.address)

    def execute(self):
        response = requests.get(self.url)
        self.response_data = json.loads(response.content.decode('utf-8'))
        coords = self.response_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        coords = list(map(float, coords))[::-1]
        return coords


class GetEventDataByEventIds:
    def __init__(self, event_ids):
        self.event_ids = event_ids

    def execute(self):
        self.threads = []
        for event_id in self.event_ids:
            self.threads.append(GetEventDataByEventId(event_id))

        for thread in self.threads:
            thread.start()

        for thread in self.threads:
            thread.join()

        self.results = []
        for thread in self.threads:
            if thread.response_data.get('coords', None):
                self.results.append(thread.response_data)

        return self.results


class GetEventDataByEventId(Thread):
    def __init__(self, event_id):
        super().__init__()
        self.event_id = event_id
        self.url = 'https://api.dobrf.ru/open-api/v1/events/{}/'.format(self.event_id)

    def execute(self):
        response = requests.get(self.url)
        self.response_data = json.loads(response.content.decode('utf-8'))
        self.response_data['coords'] = GetCoordByAddress(self.response_data['address']).execute()
        return self.response_data

    def run(self):
        try:
            self.execute()
        except:
            pass


class GetEventIdsByLocation:
    def __init__(self, location_id):
        self.location_id = location_id
        self.url = 'https://api.dobrf.ru/open-api/v1/events/?is_start_soon=true&ordering=-start_date&region={}'.format(self.location_id)

    def execute(self):
        response = requests.get(self.url)
        self.response_data = json.loads(response.content.decode('utf-8'))
        return [event['id'] for event in self.response_data['results']]
