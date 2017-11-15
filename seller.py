from flask_restful import Resource
from flask_restful.utils import cors

from dbconnector import *
from flask import request


class Seller(Resource):
    def __init__(self):
        super().__init__()
        self._sellerconnector = MongoConnector(uri="ds261745.mlab.com:61745", db="p2pscale", table="sellers",
                                              username="test",
                                              password="123456")

    @cors.crossdomain(origin='*')
    def get(self):
        parameters = dict()
        for key in request.args.keys():
            parameters[key] = request.args[key]
        return self._sellerconnector.filter(parameters)
