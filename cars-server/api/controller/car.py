from flask import jsonify
from flask_restful import Resource

from api.controller.helpers.car import car_parse
from api.controller.helpers.utils import encode_document
from api.repository import car


class Car(Resource):

    def get(self, car, car_id):
        try:
            data = car.get_car_by_id(car_id)
            success = True
        except Exception as e:
            print(e)
            data = None
            success = False
        return jsonify({'success': success, 'data': encode_document(data)})

    def post(self):
        data = car_parse.parse_args()
        try:
            car.save_car(data)
            success = True
        except Exception as e:
            print(e)
            success = False
        return jsonify({'success': success, 'data': None})

    def put(self):
        data = car_parse.parse_args()
        try:
            car.update_car(data)
            success = True
        except Exception as e:
            print(e)
            success = False
        return jsonify({'success': success, 'data': None})

    def delete(self):
        data = car_parse.parse_args()
        try:
            car.delete_car(data)
            success = True
        except Exception as e:
            print(e)
            success = False
        return jsonify({'success': success, 'data': None})


class CarList(Resource):

    def get(self):
        try:
            data = car.get_all_cars()
            success = True
        except Exception as e:
            print(e)
            data = None
            success = False

        return jsonify({'success': success, 'data': encode_document(data)})
