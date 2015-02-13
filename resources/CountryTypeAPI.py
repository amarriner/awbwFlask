#!/usr/bin/env python

from flask.ext import restful
from bson.objectid import ObjectId

from awbwFlask import mongo
from awbwFlask.common.methods import bsonToJson
from awbwFlask.common.variables import headers

class CountryType_EP(restful.Resource):

   def get(self):

      return bsonToJson(list(mongo.db.countryType.find())), 200

class CountryType_ID_EP(restful.Resource):

   country_type = None

   def get(self, id):
      self.country_type = mongo.db.countryType.find({ '_id': ObjectId(id) })

      if not self.country_type:
         return {'message': "CountryType with ID {} does not exist".format(id)}, 404, headers

      return bsonToJson(self.country_type), 200

if __name__ == '__main__':
   app.run(debug=True)
