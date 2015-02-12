#!/home1/amarrine/python/bin/python

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import relationship
from awbwFlask.resources.alchemy.AlchemyDB import Base

import json

class TerrainType(Base):
   __tablename__ = 'awbw_terrain_types'

   id = Column(Integer, primary_key=True)
   name = Column(String(40), nullable=False)
   defense = Column(Integer, nullable=False)
   symbol = Column(String(1), nullable=False)
   offset = Column(Integer, nullable=False)

   meta = MetaData()

   def __repr__(self):
      return {"TerrainType": json.dumps(self.json())}

   def create_table(self, engine):
      Base.metadata.create_all(engine)

   def costs_json(self):
      # Loops through each TerrainCost found for this terrain id and associates weather and unit
      # objects with that cost in case we need reverse lookup
      return [dict(c.json().items() +
                   {'unit_movement_type': {
                         'id': c.unit_movement_type_parent.id,
                         'code': c.unit_movement_type_parent.code,
                         'name': c.unit_movement_type_parent.name
                      }
                   }.items() +
                   {'weather_type': {
                         'id': c.weather_type_parent.id,
                         'name': c.weather_type_parent.name
                      }
                   }.items())
                   for c in self.terrain_costs]

   def json(self):
      return {
         "id"              : self.id,
         "name"            : self.name,
         "defense"         : self.defense,
         "symbol"          : self.symbol,
         "offset"          : self.offset,
         "costs"           : self.costs_json()
      }
