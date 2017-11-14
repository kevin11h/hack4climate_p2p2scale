from flask_restful import Resource

class Asset(Resource):
    def get(self):
    	products = [{"id":1, "name":"Cocoa Pack A", "price" : 1000},
    			{"id":2, "name":"Cocoa Pack B", "price" : 5000}]
    	return {'response': 'ok', 'data' : products}

    def post(self):
    	all_data = request.get_json()
    	return {'response': 'ok', 'data' : all_data}

