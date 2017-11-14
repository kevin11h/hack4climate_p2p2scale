from flask_restful import Resource
from flask import request
from dbconnector import *


class Asset(Resource):
    def __init__(self, *test):
        super().__init__()
        self._connector = MongoConnector(uri="ds261745.mlab.com:61745", db="p2pscale", table="assets", username="test",
                                         password="123456")

    def get(self):
        parameters = dict()
        for key in request.args.keys():
            parameters[key] = request.args[key]
        return self._connector.filter(parameters)

    def post(self):
        all_data = request.get_json()
        self._connector.insert(all_data)
        return {'response': 'ok'}
