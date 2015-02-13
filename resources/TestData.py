#!/usr/bin/env python

from flask.ext import restful
from awbwFlask import mongo
from awbwFlask.common.variables import headers

from bson.objectid import ObjectId
from bson.json_util import dumps
import json

class TestData_EP(restful.Resource):

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('name', type=str)
      super(TestData_EP, self).__init__()

   def get(self):
      t = mongo.db.testData.find()

      return json.loads(dumps(list(t))), 200

   def post(self):
      args = self.reqparse.parse_args()      
      print args
      mongo.db.testData.insert(args)

      return {'message': 'Inserted record!'}, 200

class TestData_ID_EP(restful.Resource):
   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('name', type=str)
      super(TestData_ID_EP, self).__init__()

   def delete(self, id):
      o = mongo.db.testData.find_one({ '_id' : ObjectId(id) })

      if not o:
         return {'message': "No such object with ID {}".format(id)}, 404, headers

      mongo.db.testData.remove({ '_id' : ObjectId(id) })

      return {'message': "Successfully deleted ID {}".format(id)}, 200

   def put(self, id):
      args = self.reqparse.parse_args()
      o = mongo.db.testData.find_one({ '_id' : ObjectId(id) })

      if not o:
         return {'message': "No such object with ID {}".format(id)}, 404, headers

      args['_id'] = ObjectId(id)
      mongo.db.testData.save(args)

      return {'message': "Successfully updated ID {}".format(id)}, 200

if __name__ == '__main__':
   app.run(debug=True)
