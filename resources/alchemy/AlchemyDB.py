#!/home1/amarrine/python/bin/python

import awbwFlask.resources.alchemy.passwd as passwd

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

class AlchemyDB():

   username = 'amarrine_amarrin'
   pwd      = passwd.db_passwd
   host     = 'localhost'
   database = 'amarrine_awbw'

   engine   = None
   session  = None

   def __init__(self):
      self.engine = create_engine('mysql+mysqldb://' + self.username + ':' + self.pwd + '@' + self.host + '/' + self.database, echo=True).connect()

      self.session = sessionmaker(bind=self.engine)()
