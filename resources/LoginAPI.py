#!/usr/bin/env python

from flask.ext import restful

from awbwFlask import mongo
from awbwFlask.common.methods import bsonToJson, generate_auth_token, hash_password, verify_auth_token, verify_password
from awbwFlask.common.variables import headers

class Login_EP(restful.Resource):

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('username', type=str, help='Invalid username')
      self.reqparse.add_argument('password', type=str, help='Invalid password')
      self.reqparse.add_argument('Awbw-Token', type=str, help='Invalid Token', location='headers')
      super(Login_EP, self).__init__()

   def post(self):
      args = self.reqparse.parse_args()

      if args['Awbw-Token']:
         token_data = verify_auth_token(args['Awbw-Token'])

         if not token_data:
            return {"message": "Invalid user token"}, 401, headers
 
         user = {'_id': token_data["_id"], 'username': token_data["username"]}
         message = "Logged in with token"

      else:

         user = mongo.db.users.find_one({ 'username': args['username'] })

         if not user:
            return {"message": "Login with username {} does not exist".format(args['username'])}, 404, headers

         if not verify_password(args['password'], user['password']):
            return {"message": "Invalid password for user {}".format(args['username'])}, 401, headers

         message = "Logged in with credentials"

      return {"message": message, "username": user["username"], "token": generate_auth_token(bsonToJson(user))}, 200

if __name__ == '__main__':
   app.run(debug=True)
