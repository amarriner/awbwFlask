#!/usr/bin/env python

from __future__ import print_function

from flask.ext import restful

from awbwFlask.common.AlchemyDB import adb
from awbwFlask.common.variables import headers
from awbwFlask.resources.alchemy.User import User

class Login_EP(restful.Resource):

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('username', type=str, help='Invalid username (required)')
      self.reqparse.add_argument('password', type=str, help='Invalid password (required)')
      self.reqparse.add_argument('Awbw-Token', type=str, help='Invalid Token', location='headers')
      super(Login_EP, self).__init__()

   def get(self):
      return {"message": "invalid"}, 400

   def post(self):
      args = self.reqparse.parse_args()

      if args['Awbw-Token']:
         token_data = User.verify_auth_token(args['Awbw-Token'])

         if not token_data:
            return {"message": "Invalid user token"}, 401, headers
 
         user = adb.session.query(User).get(token_data["id"])
         message = "Logged in with token"

      else:

         user = adb.session.query(User).filter(User.username == args['username']).first()

         if not user:
            return {"message": "Login with username {} does not exist".format(args['username'])}, 404, headers

         if not user.verify_password(args['password']):
            return {"message": "Invalid password for user {}".format(args['username'])}, 401, headers

         message = "Logged in with credentials"

      return {"message": message, "username": user.username, "token": user.generate_auth_token()}, 200

if __name__ == '__main__':
   app.run(debug=True)
