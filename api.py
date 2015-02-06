#!/home1/amarrine/python/bin/python

from flask import Flask, request
from flask.ext.restful import abort, Api, Resource, reqparse

from resources.UnitTypeAPI import UnitType_EP
from resources.UnitTypeAPI import UnitType_ID_EP

app = Flask(__name__)
api = Api(app)

api.add_resource(UnitType_EP, '/unit-type')
api.add_resource(UnitType_ID_EP, '/unit-type/<int:id>')

if __name__ == '__main__':
   app.run(debug=True)
