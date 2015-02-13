#!/usr/bin/env python

from flask.ext import restful
from bson.objectid import ObjectId

from awbwFlask import mongo
from awbwFlask.common.methods import bsonToJson
from awbwFlask.common.variables import headers

class UnitType_EP(restful.Resource):

   def get(self):
      
      return bsonToJson(list(mongo.db.unitType.find())), 200

class UnitType_ID_EP(restful.Resource):

   def get(self, id):
      unit_type = mongo.db.unitType.find({ '_id': ObjectId(id)})

      if not unit_type:
         return {'message': "UnitType with ID {} does not exist".format(id)}, 404, headers

      return bsonToJson(unit_type), 200

if __name__ == '__main__':
   app.run(debug=True)
