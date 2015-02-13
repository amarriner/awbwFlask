#!/usr/bin/env python

from flask.ext import restful
from bson.objectid import ObjectId

from awbwFlask import mongo
from awbwFlask.common.variables import headers
from awbwFlask.common.methods import bsonToJson

class TerrainType_EP(restful.Resource):

   def get(self):      
      return bsonToJson(list(mongo.db.terrainType.find())), 200

class TerrainType_ID_EP(restful.Resource):

   def get(self, id):
      terrain_type = mongo.db.terrainType.find({ '_id': ObjectId(id) })

      if not terrain_type:
         return {'message': "TerrainType with ID {} does not exist".format(id)}, 404, headers

      return bsonToJson(terrain_type), 200,

if __name__ == '__main__':
   app.run(debug=True)
