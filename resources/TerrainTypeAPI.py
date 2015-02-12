#!/home1/amarrine/python/bin/python

from flask.ext import restful

from awbwFlask.common.AlchemyDB import adb

from awbwFlask.resources.alchemy.TerrainType import TerrainType
from awbwFlask.resources.alchemy.TerrainCost import TerrainCost

class TerrainType_EP(restful.Resource):

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      super(TerrainType_EP, self).__init__()

   def get(self):
      terrain_types = []      
      for t in adb.session.query(TerrainType):
         terrain_types.append(t.json())

      return terrain_types, 200

class TerrainType_ID_EP(restful.Resource):

   terrain_type = None

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      super(TerrainType_ID_EP, self).__init__()

   def abort_if_not_exists(self, id):
      self.terrain_type = adb.session.query(TerrainType).get(id)
      if not self.terrain_type:
         restful.abort(404, message="TerrainType with ID {} does not exist".format(id))

   def get(self, id):
      self.abort_if_not_exists(id)

      return self.terrain_type.json(), 200,

if __name__ == '__main__':
   app.run(debug=True)
