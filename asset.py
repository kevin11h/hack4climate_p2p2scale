from flask_restful import Resource

class Asset(Resource):
    def post(self):
        return {'status': 'success'}