import requests
from model import Person, Film

class StarWarsService:
    BASE_URL = 'https://swapi.dev/api'

    def get_person(self, id):
        url = f'{self.BASE_URL}/people/{id}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
            # return Person(data['name'], data['height'], data['mass'])
        return None

    def get_film(self, id):
        url = f'{self.BASE_URL}/films/{id}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return Film(data['title'], data['director'], data['release_date'])
        return None
