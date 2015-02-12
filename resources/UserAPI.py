#!/home1/amarrine/python/bin/python

from flask.ext import restful

from awbwFlask.common.AlchemyDB import adb
from awbwFlask.resources.alchemy.User import User

class User_EP(restful.Resource):

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('username', required=True, type=str, help='Invalid username (required)')
      self.reqparse.add_argument('password', required=True, type=str, help='Invalid password (required)')
      super(User_EP, self).__init__()

   def post(self):
      args = self.reqparse.parse_args()

      user = adb.session.query(User).filter(User.username == args['username'])
      if user:
         restful.abort(400, message="User {} already exists".format(args['username']))

      user = User(username=args['username'])
      user.hash_password(args['password'])
      
      adb.session.add(user)
      adb.session.commit()

      return user.json(), 201

class User_ID_EP(restful.Resource):

   user = None

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      super(User_ID_EP, self).__init__()
   
   def abort_if_not_exists(self, id):
      self.user = adb.session.query(User).get(id)
      if not self.user:
         restful.abort(404, message="User with ID {} does not exist".format(id))

   def get(self, id):
      self.abort_if_not_exists(id)

      return self.user.json(), 200

   def put(self, id):
      args = self.reqparse.parse_args()
      self.abort_if_not_exists(id)

      adb.session.commit()
      return self.user.json(), 200

if __name__ == '__main__':
   app.run(debug=True)
