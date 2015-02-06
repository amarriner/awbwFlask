#!/home1/amarrine/python/bin/python

from flask.ext import restful

from awbwFlask.resources.alchemy.AlchemyDB import AlchemyDB
from awbwFlask.resources.alchemy.UnitType import UnitType

class UnitType_EP(restful.Resource):

   adb = AlchemyDB()

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('name', required=True, type=str, help='Invalid name (required)')
      self.reqparse.add_argument('movement_points', required=True, type=int, help='Invalid movement points (required)')
      self.reqparse.add_argument('movement_type', required=True, type=str, help='Invalid movement type (required)')
      self.reqparse.add_argument('ammo', required=True, type=int, help='Invalid ammo (required)')
      self.reqparse.add_argument('vision', required=True, type=int, help='Invalid vision (required)')
      self.reqparse.add_argument('short_range', required=True, type=int, help='Invalid short range (required)')
      self.reqparse.add_argument('long_range', required=True, type=int, help='Invalid long range (required)')
      self.reqparse.add_argument('cost', required=True, type=int, help='Invalid cost (required)')
      super(UnitType_EP, self).__init__()

   def get(self):
      unit_types = []      
      for u in self.adb.session.query(UnitType):
         unit_types.append(u.json())

      return unit_types, 200

   def post(self):
      args = self.reqparse.parse_args()

      unit_type = UnitType(
                  name=args['name'],
                  movement_points=args['movement_points'],
                  movement_type=args['movement_type'],
                  ammo=args['ammo'],
                  vision=args['vision'],
                  short_range=args['short_range'],
                  long_range=args['long_range'],
                  cost=args['cost']
             )   
      
      self.adb.session.add(unit_type)
      self.adb.session.commit()
      return unit_type.json(), 201

class UnitType_ID_EP(restful.Resource):

   adb = AlchemyDB()
   unit_type = None

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('name', type=str, help='Invalid name (required)')
      self.reqparse.add_argument('movement_points', type=int, help='Invalid movement points (required)')
      self.reqparse.add_argument('movement_type', type=str, help='Invalid movement type (required)')
      self.reqparse.add_argument('ammo', type=int, help='Invalid ammo (required)')
      self.reqparse.add_argument('vision', type=int, help='Invalid vision (required)')
      self.reqparse.add_argument('short_range', type=int, help='Invalid short range (required)')
      self.reqparse.add_argument('long_range', type=int, help='Invalid long range (required)')
      self.reqparse.add_argument('cost', type=int, help='Invalid cost (required)')
      super(UnitType_ID_EP, self).__init__()

   def abort_if_not_exists(self, id):
      self.unit_type = self.adb.session.query(UnitType).get(id)
      if not self.unit_type:
         restful.abort(404, message="UnitType with ID {} does not exist".format(id))

   def get(self, id):
      self.abort_if_not_exists(id)

      return self.unit_type.json(), 200

   def delete(self, id):
      self.abort_if_not_exists(id)
      self.adb.session.delete(self.unit_type)
      self.adb.session.commit()
      return { "message": "UnitType " + str(id) + " deleted"}, 200

   def put(self, id):
      args = self.reqparse.parse_args()
      self.abort_if_not_exists(id)
      
      self.unit_type.name            = args['name']            if args['name']            else self.unit_type.name
      self.unit_type.movement_points = args['movement_points'] if args['movement_points'] else self.unit_type.movement_points
      self.unit_type.movement_type   = args['movement_type']   if args['movement_type']   else self.unit_type.movement_type
      self.unit_type.ammo            = args['ammo']            if args['ammo']            else self.unit_type.ammo
      self.unit_type.vision          = args['vision']          if args['vision']          else self.unit_type.vision
      self.unit_type.short_range     = args['short_range']     if args['short_range']     else self.unit_type.short_range
      self.unit_type.long_range      = args['long_range']      if args['long_range']      else self.unit_type.long_range
      self.unit_type.cost            = args['cost']            if args['cost']            else self.unit_type.cost

      self.adb.session.commit()
      return self.unit_type.json(), 200

if __name__ == '__main__':
   app.run(debug=True)
