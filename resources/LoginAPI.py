#!/home1/amarrine/python/bin/python

from __future__ import print_function

from flask.ext import restful

from awbwFlask.resources.alchemy.AlchemyDB import AlchemyDB
from awbwFlask.resources.alchemy.User import User

from awbwFlask.common.variables import headers

class Login_EP(restful.Resource):

   adb = AlchemyDB()

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('username', type=str, help='Invalid username (required)')
      self.reqparse.add_argument('password', type=str, help='Invalid password (required)')
      self.reqparse.add_argument('Awbw-Token', type=str, help='Invalid Token', location='headers')
      super(Login_EP, self).__init__()

   def get(self):
      return {"message": "invalid"}, 400, headers

   def post(self):
      args = self.reqparse.parse_args()

      if args['Awbw-Token']:
         token_data = User.verify_auth_token(args['Awbw-Token'])

         if not token_data:
            return {"message": "Invalid user token"}, 401, headers
 
         user = self.adb.session.query(User).get(token_data["id"])
         message = "Logged in with token"

      else:

         user = self.adb.session.query(User).filter(User.username == args['username']).first()

         if not user:
            return {"message": "Login with username {} does not exist".format(args['username'])}, 404, headers

         if not user.verify_password(args['password']):
            return {"message": "Invalid password for user {}".format(args['username'])}, 403, headers

         message = "Logged in with credentials"

      return {"message": message, "username": user.username, "token": user.generate_auth_token()}, 200, headers

if __name__ == '__main__':
   app.run(debug=True)
