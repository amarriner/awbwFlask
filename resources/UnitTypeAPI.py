#!/home1/amarrine/python/bin/python

from flask.ext import restful

from awbwFlask.common.AlchemyDB import adb
from awbwFlask.resources.alchemy.UnitType import UnitType

class UnitType_EP(restful.Resource):

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      super(UnitType_EP, self).__init__()

   def get(self):
      unit_types = []      
      for u in adb.session.query(UnitType):
         unit_types.append(u.json())

      return unit_types, 200

class UnitType_ID_EP(restful.Resource):

   unit_type = None

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      super(UnitType_ID_EP, self).__init__()

   def abort_if_not_exists(self, id):
      self.unit_type = adb.session.query(UnitType).get(id)
      if not self.unit_type:
         restful.abort(404, message="UnitType with ID {} does not exist".format(id))

   def get(self, id):
      self.abort_if_not_exists(id)

      return self.unit_type.json(), 200

if __name__ == '__main__':
   app.run(debug=True)
