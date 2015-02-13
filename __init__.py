#!/usr/bin/env python

import sys

sys.path.append('/home/amarriner/awbwFlask')

from flask import Flask, request
from flask.ext.restful import abort, Api, Resource, reqparse
from flask.ext.pymongo import PyMongo

app = Flask('awbwFlask')
api = Api(app)
mongo = PyMongo(app)

if __name__ == '__main__':
   app.run(debug=True)
