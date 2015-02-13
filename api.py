#!/usr/bin/env python

import sys
from awbwFlask import api, app, mongo

sys.path.append('/home/amarriner/awbwFlask')

from awbwFlask.resources.CountryTypeAPI import CountryType_EP, CountryType_ID_EP
from awbwFlask.resources.UnitTypeAPI import UnitType_EP, UnitType_ID_EP
from awbwFlask.resources.UserAPI import User_EP, User_ID_EP
from awbwFlask.resources.TerrainTypeAPI import TerrainType_EP, TerrainType_ID_EP
from awbwFlask.resources.LoginAPI import Login_EP

api.add_resource(CountryType_EP, '/api/country-type')
api.add_resource(CountryType_ID_EP, '/api/country-type/<string:id>')

api.add_resource(UnitType_EP, '/api/unit-type')
api.add_resource(UnitType_ID_EP, '/api/unit-type/<string:id>')

api.add_resource(User_EP, '/api/user')
api.add_resource(User_ID_EP, '/api/user/<string:id>')

api.add_resource(TerrainType_EP, '/api/terrain-type')
api.add_resource(TerrainType_ID_EP, '/api/terrain-type/<string:id>')

api.add_resource(Login_EP, '/api/login')

if __name__ == '__main__':
   app.run(debug=True)
