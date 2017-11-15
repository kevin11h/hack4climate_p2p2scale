from flask import Flask
from flask_restful import Api
from asset import Asset
from buyer import Buyer
from seller import *
import os
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Asset, '/Assets')
api.add_resource(Seller, '/Sellers')
api.add_resource(Buyer, '/Buyers')


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


