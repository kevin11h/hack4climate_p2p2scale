from flask_restful import Resource
from flask import request
from dbconnector import *


class Asset(Resource):
    def __init__(self):
        super().__init__()
        self._assetconnector = MongoConnector(uri="ds261745.mlab.com:61745", db="p2pscale", table="assets", username="test",
                                              password="123456")
        self._sellerconnector = MongoConnector(uri="ds261745.mlab.com:61745", db="p2pscale", table="sellers",
                                              username="test",
                                              password="123456")

    def get(self):
        parameters = dict()
        for key in request.args.keys():
            parameters[key] = request.args[key]
        return self._assetconnector.filter(parameters)

    def post(self):
        all_data = request.get_json()
        if len(all_data) == 1:
            _, values = all_data.popitem()
            self.store_multiple_records(values)
        else:
            self.store_single_multicolumn_record(all_data)
        return {'response': 'ok'}

    def store_single_multicolumn_record(self, all_data):
        all_data["hash"] = create_hash(str(all_data))
        self._assetconnector.insert(all_data)
        result = self._sellerconnector.filter({'clientid':all_data["clientid"]})
        if result:
            self._sellerconnector.update({'clientid': result[0]["clientid"]}, {"sum": result[0]["sum"]+ all_data["amount"]})
        else:
            self._sellerconnector.insert({'clientid': all_data["clientid"], "sum": all_data["amount"]})

    def store_multiple_records(self, values):
        for value in values:
            value["hash"] = create_hash(str(value))
            result = self._sellerconnector.filter({'clientid':value["clientid"]})
            if result:
                self._sellerconnector.update({'clientid': result["clientid"]},
                                             {"sum": result["sum"] + value["amount"]})
            else:
                self._sellerconnector.insert({'clientid': result["clientid"], "sum": value["amount"]})
        self._assetconnector.insert(values)
