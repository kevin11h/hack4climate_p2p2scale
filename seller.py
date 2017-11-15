from flask_restful import Resource
from flask import request


class Seller(Resource):
    def get(self):
        sellers = [{"id": 1, "name": "Seller Farmer A", "address": "Some place in Ivory Coast"},
                   {"id": 2, "name": "Seller Farmer B", "address": "Some place near beach in Ivory Coast"}]
        return {'response': 'ok', 'data': sellers}
