from flask import jsonify
from services import StarWarsService

class StarWarsController:
    def __init__(self):
        self.service = StarWarsService()

    def get_person(self, id):
        person = self.service.get_person(id)
        if person:
            return jsonify(person)
        else:
            return jsonify({'error': 'Person not found'}), 404

    def get_film(self, id):
        film = self.service.get_film(id)
        if film:
            return jsonify(film)
        else:
            return jsonify({'error': 'Film not found'}), 404
