from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api

from api.controller.car import Car

app = Flask(__name__)

# Configure CORS
cors = CORS(app,  origins=['http://localhost:8080'])

app.config['MONGO_URI'] = 'mongodb://3.14.7.212:27017/Cars'
app.database = PyMongo(app)
app.cards_collection = app.database.db.cars

# Create API
api = Api(app)

api.add_resource(Car, '/car', '/car/<car_id>',
                 methods=['GET', 'POST', 'PUT', 'DELETE'])
