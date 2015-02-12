#!/home1/amarrine/python/bin/python

from flask.ext import restful

from awbwFlask.common.AlchemyDB import adb

from awbwFlask.resources.alchemy.CountryType import CountryType

class CountryType_EP(restful.Resource):

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      super(CountryType_EP, self).__init__()

   def get(self):
      country_types = []      
      for c in adb.session.query(CountryType):
         country_types.append(c.json())

      return country_types, 200

class CountryType_ID_EP(restful.Resource):

   country_type = None

   def __init__(self):
      self.reqparse = restful.reqparse.RequestParser()
      super(CountryType_ID_EP, self).__init__()

   def abort_if_not_exists(self, id):
      self.country_type = adb.session.query(CountryType).get(id)
      if not self.country_type:
         restful.abort(404, message="CountryType with ID {} does not exist".format(id))

   def get(self, id):
      self.abort_if_not_exists(id)

      return self.country_type.json(), 200,

if __name__ == '__main__':
   app.run(debug=True)
