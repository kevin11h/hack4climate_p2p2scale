from flask import request
from flask_restful import Resource
from flask_restful.utils import cors

from dbconnector import *


class Buyer(Resource):
    def __init__(self):
        super().__init__()
        self._assetconnector = MongoConnector(uri="ds261745.mlab.com:61745", db="p2pscale", table="assets",
                                              username="test",
                                              password="123456")
        self._sellerconnector = MongoConnector(uri="ds261745.mlab.com:61745", db="p2pscale", table="sellers",
                                               username="test",
                                               password="123456")
        self._buyerconnector = MongoConnector(uri="ds261745.mlab.com:61745", db="p2pscale", table="buyers",
                                              username="test",
                                              password="123456")

    @cors.crossdomain(origin='*')
    def post(self):
        all_data = request.get_json()
        offers = all_data["hashes"]
        updates = []
        for offer in offers:
            asset = self._assetconnector.filter({"hash": offer})[0]
            seller = self._sellerconnector.filter(
                {"clientid": asset["clientid"]})
            newsum = seller[0]["sum"] - asset["amount"]
            if newsum<0:
                return {"response": "invalid"}
            updates.append([seller[0]["clientid"], newsum])

        for clientid, sum in updates:
            self._sellerconnector.update({"clientid": clientid}, {"sum": sum})
            self._buyerconnector.insert(all_data)

        return {"response":"ok"}
