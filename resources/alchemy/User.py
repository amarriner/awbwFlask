#!/home1/amarrine/python/bin/python

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from passlib.apps import custom_app_context as pwd_context

import json

Base = declarative_base()

class User(Base):
   __tablename__ = 'awbw_users'

   id = Column(Integer, primary_key=True)
   username = Column(String(40), index=True, nullable=False)
   password_hash = Column(String(128), nullable=False)

   meta = MetaData()

   def __repr__(self):
      return json.dumps({"User": json.dumps(self.json())})

   def create_table(self, engine):
      Base.metadata.create_all(engine)

   def json(self):
      return {
         "id"              : self.id,
         "username"        : self.username
      }

   def hash_password(self, password):
      self.password_hash = pwd_context.encrypt(password)

   def verify_password(self, password):
      return pwd_context.verify(password, self.password_hash)
