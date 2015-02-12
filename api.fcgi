#!/usr/bin/env python

from flup.server.fcgi import WSGIServer
from api import app

import os,sys

sys.path.append("/home/amarriner/awbwFlask")
 
if __name__ == '__main__':
   WSGIServer(app).run()
