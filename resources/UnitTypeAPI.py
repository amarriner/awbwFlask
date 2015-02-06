#!/home1/amarrine/python/bin/python

from flask.ext import restful

from awbwFlask.resources.alchemy.AlchemyDB import AlchemyDB
from awbwFlask.resources.alchemy.UnitType import UnitType

from awbwFlask.common.variables import headers

class UnitType_EP(restful.Resource):

   adb = AlchemyDB()

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('name', required=True, type=str, help='Invalid name (required)')
      self.reqparse.add_argument('movementPoints', required=True, type=int, help='Invalid movement points (required)')
      self.reqparse.add_argument('movementType', required=True, type=str, help='Invalid movement type (required)')
      self.reqparse.add_argument('ammo', required=True, type=int, help='Invalid ammo (required)')
      self.reqparse.add_argument('vision', required=True, type=int, help='Invalid vision (required)')
      self.reqparse.add_argument('shortRange', required=True, type=int, help='Invalid short range (required)')
      self.reqparse.add_argument('longRange', required=True, type=int, help='Invalid long range (required)')
      self.reqparse.add_argument('cost', required=True, type=int, help='Invalid cost (required)')
      self.reqparse.add_argument('fuel', required=True, type=int, help='Invalid fuel (required)')
      self.reqparse.add_argument('fuelPerTurn', required=True, type=int, help='Invalid fuel per turn (required)')
      self.reqparse.add_argument('secondWeapon', required=True, type=int, help='Invalid second weapon (required)')
      self.reqparse.add_argument('symbol', required=True, type=str, help='Invalid symbol (required)')
      super(UnitType_EP, self).__init__()

   def get(self):
      unit_types = []      
      for u in self.adb.session.query(UnitType):
         unit_types.append(u.json())

      return unit_types, 200, headers

   def post(self):
      args = self.reqparse.parse_args()

      unit_type = UnitType(
                  name            = args['name'],
                  movement_points = args['movementPoints'],
                  movement_type   = args['movementType'],
                  ammo            = args['ammo'],
                  vision          = args['vision'],
                  short_range     = args['shortRange'],
                  long_range      = args['longRange'],
                  cost            = args['cost'],
                  fuel            = args['fuel'],
                  fuel_per_turn   = args['fuelPerTurn'],
                  second_weapon   = args['secondWeapon'],
                  symbol          = args['symbol']
             )   
      
      self.adb.session.add(unit_type)
      self.adb.session.commit()
      return unit_type.json(), 201, headers

class UnitType_ID_EP(restful.Resource):

   adb = AlchemyDB()
   unit_type = None

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      self.reqparse.add_argument('name', type=str, help='Invalid name')
      self.reqparse.add_argument('movementPoints', type=int, help='Invalid movement points')
      self.reqparse.add_argument('movementType', type=str, help='Invalid movement type')
      self.reqparse.add_argument('ammo', type=int, help='Invalid ammo')
      self.reqparse.add_argument('vision', type=int, help='Invalid vision')
      self.reqparse.add_argument('shortRange', type=int, help='Invalid short range')
      self.reqparse.add_argument('longRange', type=int, help='Invalid long range')
      self.reqparse.add_argument('cost', type=int, help='Invalid cost')
      self.reqparse.add_argument('fuel', type=int, help='Invalid fuel')
      self.reqparse.add_argument('fuelPerTurn', type=int, help='Invalid fuel per turn')
      self.reqparse.add_argument('secondWeapon', type=int, help='Invalid second weapon')
      self.reqparse.add_argument('symbol', type=str, help='Invalid symbol')
      super(UnitType_ID_EP, self).__init__()

   def abort_if_not_exists(self, id):
      self.unit_type = self.adb.session.query(UnitType).get(id)
      if not self.unit_type:
         restful.abort(404, message="UnitType with ID {} does not exist".format(id), headers=headers)

   def get(self, id):
      self.abort_if_not_exists(id)

      return self.unit_type.json(), 200, headers

   def delete(self, id):
      self.abort_if_not_exists(id)
      self.adb.session.delete(self.unit_type)
      self.adb.session.commit()
      return { "message": "UnitType " + str(id) + " deleted"}, 200, headers

   def put(self, id):
      args = self.reqparse.parse_args()
      self.abort_if_not_exists(id)
      
      self.unit_type.name            = args['name']            if args['name']            else self.unit_type.name
      self.unit_type.movement_points = args['movementPoints']  if args['movementPoints']  else self.unit_type.movement_points
      self.unit_type.movement_type   = args['movementType']    if args['movementType']    else self.unit_type.movement_type
      self.unit_type.ammo            = args['ammo']            if args['ammo']            else self.unit_type.ammo
      self.unit_type.vision          = args['vision']          if args['vision']          else self.unit_type.vision
      self.unit_type.short_range     = args['shortRange']      if args['shortRange']      else self.unit_type.short_range
      self.unit_type.long_range      = args['longRange']       if args['longRange']       else self.unit_type.long_range
      self.unit_type.cost            = args['cost']            if args['cost']            else self.unit_type.cost
      self.unit_type.fuel            = args['fuel']            if args['fuel']            else self.unit_type.fuel
      self.unit_type.fuel_per_turn   = args['fuelPerTurn']     if args['fuelPerTurn']     else self.unit_type.fuel_per_turn
      self.unit_type.second_weapon   = args['secondWeapon']    if args['secondWeapon']    else self.unit_type.second_weapon
      self.unit_type.symbol          = args['symbol']          if args['symbol']          else self.unit_type.symbol

      self.adb.session.commit()
      return self.unit_type.json(), 200, headers

if __name__ == '__main__':
   app.run(debug=True)
