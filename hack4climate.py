from flask import Flask
from flask_restful import Api
from asset import Asset
from seller import *



app = Flask(__name__)
api = Api(app)

api.add_resource(Asset, '/Assets')
api.add_resource(Seller, '/Sellers')


if __name__ == '__main__':
    app.run(debug=True)


