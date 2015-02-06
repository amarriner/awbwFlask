#!/home1/amarrine/python/bin/python

import sys

sys.path.append('/home1/amarrine/python/projects')

from flask import Flask, request
from flask.ext.restful import abort, Api, Resource, reqparse

from awbwFlask.resources.UnitTypeAPI import UnitType_EP
from awbwFlask.resources.UnitTypeAPI import UnitType_ID_EP

from awbwFlask.resources.UserAPI import User_EP
from awbwFlask.resources.UserAPI import User_ID_EP

from awbwFlask.resources.LoginAPI import Login_EP

app = Flask(__name__)
api = Api(app)

api.add_resource(UnitType_EP, '/unit-type')
api.add_resource(UnitType_ID_EP, '/unit-type/<int:id>')

api.add_resource(User_EP, '/user')
api.add_resource(User_ID_EP, '/user/<int:id>')

api.add_resource(Login_EP, '/login',)

if __name__ == '__main__':
   app.run(debug=True)
