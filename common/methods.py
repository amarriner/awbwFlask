#!/usr/bin/env python

from bson.objectid import ObjectId
from bson.json_util import dumps

from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

import ConfigParser
import json

def bsonToJson(bson):
   return json.loads(dumps(bson))

def hash_password(password):
   return pwd_context.encrypt(password)

def verify_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)

def generate_auth_token(user, expiration = 600):
   Config = ConfigParser.ConfigParser()
   Config.read('db.ini')

   s = Serializer(Config.get('Authorization', 'Secret'), expires_in = expiration)
   return s.dumps({ "_id": user['_id'], "username": user['username'] })

def verify_auth_token(token):
   Config = ConfigParser.ConfigParser()
   Config.read('db.ini')

   s = Serializer(Config.get('Authorization', 'Secret'))
   try:
      data = s.loads(token)
   except SignatureExpired:
      return None
   except BadSignature:
      return None

   return data
