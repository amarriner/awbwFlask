#!/usr/bin/env python

from bson.objectid import ObjectId
from bson.json_util import dumps
import json

def bsonToJson(bson):
   return json.loads(dumps(bson))
