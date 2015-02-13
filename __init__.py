#!/usr/bin/env python

import sys

sys.path.append('/home/amarriner/awbwFlask')

from flask import Flask, request
from flask.ext.restful import abort, Api, Resource, reqparse
from flask.ext.pymongo import PyMongo

import  awbwFlask.resources.alchemy.passwd as passwd

app = Flask('awbwFlask')
api = Api(app)
#app.config['MONGO_URI'] = 'mongodb://awbwFlask:' + str(passwd) + '@localhost:27017/awbwFlask'
mongo = PyMongo(app)

#from awbwFlask.resources.CountryTypeAPI import CountryType_EP, CountryType_ID_EP
#from awbwFlask.resources.UnitTypeAPI import UnitType_EP, UnitType_ID_EP
#from awbwFlask.resources.UserAPI import User_EP, User_ID_EP
#from awbwFlask.resources.TerrainTypeAPI import TerrainType_EP, TerrainType_ID_EP
#from awbwFlask.resources.LoginAPI import Login_EP

#from awbwFlask.resources.TestData import TestData_EP

#api.add_resource(CountryType_EP, '/api/country-type')
#api.add_resource(CountryType_ID_EP, '/api/country-type/<int:id>')

#api.add_resource(UnitType_EP, '/api/unit-type')
#api.add_resource(UnitType_ID_EP, '/api/unit-type/<int:id>')

#api.add_resource(User_EP, '/api/user')
#api.add_resource(User_ID_EP, '/api/user/<int:id>')

#api.add_resource(TerrainType_EP, '/api/terrain-type')
#api.add_resource(TerrainType_ID_EP, '/api/terrain-type/<int:id>')

#api.add_resource(Login_EP, '/api/login')

#api.add_resource(TestData_EP, '/api/test-data')

if __name__ == '__main__':
   app.run(debug=True)
