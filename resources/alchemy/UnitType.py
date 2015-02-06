#!/home1/amarrine/python/bin/python

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import json

Base = declarative_base()

class UnitType(Base):
   __tablename__ = 'awbw_unit_types'

   id = Column(Integer, primary_key=True)
   name = Column(String(40), nullable=False)
   movement_points = Column(Integer, nullable=False)
   movement_type = Column(String(1), nullable=False)
   ammo = Column(Integer, nullable=False)
   vision = Column(Integer, nullable=False)
   short_range = Column(Integer, nullable=False)
   long_range = Column(Integer, nullable=False)
   cost = Column(Integer, nullable=False)

   meta = MetaData()

   def __repr__(self):
      return {"UnitType": json.dumps(self.json())}

   def create_table(self, engine):
      Base.metadata.create_all(engine)

   def json(self):
      return {
         "id"              : self.id,
         "name"            : self.name,
         "movement_points" : self.movement_points if self.movement_points != None else '',
         "movement_type"   : self.movement_type if self.movement_type != None else '',
         "ammo"            : self.ammo if self.ammo != None else '',
         "vision"          : self.vision if self.vision != None else '',
         "short_range"     : self.short_range if self.short_range != None else '',
         "long_range"      : self.long_range if self.long_range != None else '',
         "cost"            : self.cost if self.cost != None else ''
      }
