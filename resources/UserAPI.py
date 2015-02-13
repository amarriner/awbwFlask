#!/usr/bin/env python

from flask.ext import restful
from bson.objectid import ObjectId
from bson.errors import InvalidId

from awbwFlask import mongo
from awbwFlask.common.methods import bsonToJson, hash_password
from awbwFlask.common.variables import headers

class User_EP(restful.Resource):

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('username', required=True, type=str, help='Invalid username (required)')
      self.reqparse.add_argument('password', required=True, type=str, help='Invalid password (required)')
      super(User_EP, self).__init__()

   def post(self):
      args = self.reqparse.parse_args()

      user = mongo.db.users.find_one({ 'username': args['username'] })
      if user:
         return {'message': "User {} already exists".format(args['username'])}, 400, headers

      user = {
         'username': args['username'],
         'password': hash_password(args['password'])
      }

      mongo.db.users.insert(user)      

      return {'message': "User {} created".format(args['username'])}, 201

class User_ID_EP(restful.Resource):

   user = None

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('password', type=str, help='Invalid password (required)')
      super(User_ID_EP, self).__init__()
   
   def get(self, id):
      
      try:
         self.user = mongo.db.users.find_one({ '_id': ObjectId(id) }, { 'password': False})
         if not self.user:
            return {'message': "User with ID {} does not exist".format(id)}, 404, headers
      except InvalidId:
         return {'message': "Invalid ID {}".format(id)}, 400, headers

      return bsonToJson(self.user), 200

   def put(self, id):
      args = self.reqparse.parse_args()

      try:
         self.user = mongo.db.users.find_one({ '_id': ObjectId(id) }, { 'password': False})
         if not self.user:
            return {'message': "User with ID {} does not exist".format(id)}, 404, headers
      except InvalidId:
         return {'message': "Invalid ID {}".format(id)}, 400, headers

      # mongo.db.users.update({ '_id': ObjectId(id)}, { $set: { 'password': hash_password(args['password'])} })
      return bsonToJson(self.user), 200

if __name__ == '__main__':
   app.run(debug=True)
