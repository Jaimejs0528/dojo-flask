from flask_restful import reqparse

car_parse = reqparse.RequestParser()
car_parse.add_argument('brand', type=str, required=True, help='no car brand')
car_parse.add_argument('model', type=str, required=True, help='no car model')
car_parse.add_argument('year', type=int, required=True, help='no car year')
car_parse.add_argument('price', type=int, required=True, help='no car price')
car_parse.add_argument('_id', type=str, required=False)
car_parse.add_argument('image', type=str, required=False)
car_parse.add_argument('sold', type=bool, required=False)