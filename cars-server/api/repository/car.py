from flask import current_app
from bson.objectid import ObjectId


def get_all_cars():
    try:
        data = current_app.cars_collection.find({})
    except Exception as e:
        print(e)
        data = None
    return data


def get_car_by_id(id_car):
    try:
        data = current_app.cars_collection.find_one({
            '_id': ObjectId(id_car)
        })
    except Exception as e:
        print(e)
        data = None
    return data


def save_car(car):
    try:
        current_app.cars_collection.insert(car)
    except Exception as e:
        print(e)


def update_car(car):
    try:
        query = {'_id': ObjectId(car.pop('id'))}
        current_app.cars_collection.update(
            query, {'$set': car}, upsert=False
        )
    except Exception as e:
        print(e)


def delete_car(id_car):
    try:
        current_app.cars_collection.remove({
            '_id': ObjectId(id_car)
            })
    except Exception as e:
        print(e)
