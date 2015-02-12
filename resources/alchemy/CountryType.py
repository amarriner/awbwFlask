#!/home1/amarrine/python/bin/python

from sqlalchemy import MetaData, Column, Integer, String
from awbwFlask.resources.alchemy.AlchemyDB import Base

import json

class CountryType(Base):
   __tablename__ = 'awbw_country_types'

   id = Column(Integer, primary_key=True)
   code = Column(String(2), nullable=False)
   name = Column(String(40), nullable=False)

   meta = MetaData()

   def __repr__(self):
      return {"CountryType": json.dumps(self.json())}

   def create_table(self, engine):
      Base.metadata.create_all(engine)

   def json(self):
      return {
         "id"              : self.id,
         "code"            : self.code,
         "name"            : self.name,
      }
