#!/home1/amarrine/python/bin/python

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import relationship
from awbwFlask.resources.alchemy.AlchemyDB import Base

import json

class WeatherType(Base):
   __tablename__ = 'awbw_weather_types'

   id = Column(Integer, primary_key=True)
   name = Column(String(40), nullable=False)

   meta = MetaData()

   def __repr__(self):
      return {"WeatherType": json.dumps(self.json())}

   def create_table(self, engine):
      Base.metadata.create_all(engine)

   def costs_json(self):
      return [dict(c.json().items() + 
                {'unit_movement_type': {
                      'id': c.unit_movement_type_parent.id, 
                      'code': c.unit_movement_type_parent.code,
                      'name': c.unit_movement_type_parent.name
                   }
                }.items() +
                {'terrain_type': {
                      'id': c.terrain_type_parent.id,
                      'name': c.terrain_type_parent.name,
                      'defense': c.terrain_type_parent.defense,
                      'symbol': c.terrain_type_parent.symbol,
                      'offset': c.terrain_type_parent.offset
                   }
                }.items())
                for c in self.weather_costs]

   def json(self):
      return {
         "id"              : self.id,
         "name"            : self.name,
         "costs"           : self.costs_json()
      }

