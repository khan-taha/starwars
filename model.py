from json import JSONEncoder

class Person:
    def __init__(self, name, height, mass):
        self.name = name
        self.height = height
        self.mass = mass

class Film:
    def __init__(self, title, director, release_date):
        self.title = title
        self.director = director
        self.release_date = release_date

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Person, Film)):
            return obj.__dict__
        return super().default(obj)