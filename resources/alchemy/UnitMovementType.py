#!/home1/amarrine/python/bin/python

from sqlalchemy import MetaData, Column, Integer, String
from awbwFlask.resources.alchemy.AlchemyDB import Base

import json

class UnitMovementType(Base):
   __tablename__ = 'awbw_unit_movement_types'

   id = Column(Integer, primary_key=True)
   code = Column(String(1), nullable=False)
   name = Column(String(40), nullable=False)

   meta = MetaData()

   def __repr__(self):
      return {"UnitMovementType": json.dumps(self.json())}

   def create_table(self, engine):
      Base.metadata.create_all(engine)

   def costs_json(self):
      return [dict(c.json().items() +
                 {'terrain_type': {
                       'id': c.terrain_type_parent.id,
                       'name': c.terrain_type_parent.name,
                       'defense': c.terrain_type_parent.defense,
                       'symbol': c.terrain_type_parent.symbol,
                       'offset': c.terrain_type_parent.offset
                    }
                 }.items() + 
                 {'weather_type': {
                       'id': c.weather_type_parent.id,
                       'name': c.weather_type_parent.name
                    }
                 }.items())
                 for c in self.unit_movement_type_costs]


   def json(self):
      return {
         "id"              : self.id,
         "code"            : self.code,
         "name"            : self.name,
         "costs"           : self.costs_json()
      }

