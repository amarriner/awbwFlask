#!/home1/amarrine/python/bin/python

from flup.server.fcgi import WSGIServer
from api import app

import os,sys

sys.path.append("/home1/amarrine/python/projects/awbwFlask")
 
if __name__ == '__main__':
   WSGIServer(app).run()
