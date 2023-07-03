from flask import Flask, jsonify
from controller import StarWarsController
from model import CustomJSONEncoder

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

# Create an instance of the controller
controller = StarWarsController()

# Define the API endpoints
app.add_url_rule('/people/<int:id>', 'get_person', controller.get_person)
app.add_url_rule('/films/<int:id>', 'get_film', controller.get_film)

if __name__ == '__main__':
    app.run()
