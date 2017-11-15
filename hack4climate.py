from flask import Flask
from flask_restful import Api
from asset import Asset
from seller import *



app = Flask(__name__)
api = Api(app)

api.add_resource(Asset, '/Assets')
api.add_resource(Seller, '/Sellers')


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


