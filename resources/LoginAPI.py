#!/home1/amarrine/python/bin/python

from flask.ext import restful

from awbwFlask.resources.alchemy.AlchemyDB import AlchemyDB
from awbwFlask.resources.alchemy.User import User

class Login_EP(restful.Resource):

   adb = AlchemyDB()

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('username', required=True, type=str, help='Invalid username (required)')
      self.reqparse.add_argument('password', required=True, type=str, help='Invalid password (required)')
      super(Login_EP, self).__init__()

   def post(self):
      args = self.reqparse.parse_args()
      user = self.adb.session.query(User).filter(User.username == args['username']).first()

      if not user:
         restful.abort(404, message="Login with username {} does not exist".format(args['username']))

      if not user.verify_password(args['password']):
         restful.abort(403, message="Invalid password for user {}".format(args['username']))

      return {"token": user.generate_auth_token()}, 200

if __name__ == '__main__':
   app.run(debug=True)
