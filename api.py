#!/home1/amarrine/python/bin/python

import sys

sys.path.append('/home1/amarrine/python/projects')

from flask import Flask, request
from flask.ext.restful import abort, Api, Resource, reqparse

from awbwFlask.resources.CountryTypeAPI import CountryType_EP, CountryType_ID_EP
from awbwFlask.resources.UnitTypeAPI import UnitType_EP, UnitType_ID_EP
from awbwFlask.resources.UserAPI import User_EP, User_ID_EP
from awbwFlask.resources.TerrainTypeAPI import TerrainType_EP, TerrainType_ID_EP
from awbwFlask.resources.LoginAPI import Login_EP

app = Flask(__name__)
api = Api(app)

api.add_resource(CountryType_EP, '/country-type')
api.add_resource(CountryType_ID_EP, '/country-type/<int:id>')

api.add_resource(UnitType_EP, '/unit-type')
api.add_resource(UnitType_ID_EP, '/unit-type/<int:id>')

api.add_resource(User_EP, '/user')
api.add_resource(User_ID_EP, '/user/<int:id>')

api.add_resource(TerrainType_EP, '/terrain-type')
api.add_resource(TerrainType_ID_EP, '/terrain-type/<int:id>')

api.add_resource(Login_EP, '/login',)

if __name__ == '__main__':
   app.run(debug=True)
