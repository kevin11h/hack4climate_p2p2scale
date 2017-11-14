from flask import Flask
from flask_restful import Api
from asset import Asset


app = Flask(__name__)
api = Api(app)

api.add_resource(Asset, '/Asset')

if __name__ == '__main__':
    app.run(debug=True)
