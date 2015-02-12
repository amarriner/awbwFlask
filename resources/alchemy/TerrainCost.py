#!/home1/amarrine/python/bin/python

from sqlalchemy import ForeignKey, MetaData, Column, Integer, String
from sqlalchemy.orm import relationship
from awbwFlask.resources.alchemy.AlchemyDB import Base
from awbwFlask.resources.alchemy.TerrainType import TerrainType
from awbwFlask.resources.alchemy.WeatherType import WeatherType
from awbwFlask.resources.alchemy.UnitMovementType import UnitMovementType

import json

class TerrainCost(Base):
   __tablename__ = 'awbw_terrain_costs'

   id = Column(Integer, primary_key=True)
   terrain_id = Column(Integer, ForeignKey("awbw_terrain_types.id"), nullable=False)
   terrain_type_parent = relationship("TerrainType", backref="terrain_costs")
   weather_id = Column(Integer, ForeignKey("awbw_weather_types.id"), nullable=False)
   weather_type_parent = relationship("WeatherType", backref="weather_costs")
   unit_movement_type_id = Column(Integer, ForeignKey("awbw_unit_movement_types.id"), nullable=False)
   unit_movement_type_parent = relationship("UnitMovementType", backref="unit_movement_type_costs")
   cost = Column(Integer, nullable=False)

   meta = MetaData()

   def __repr__(self):
      return {"TerrainCost": self.json()}

   def create_table(self, engine):
      Base.metadata.create_all(engine)

   def json(self):
      return {
         "id"              : self.id,
         "cost"            : self.cost
      }

