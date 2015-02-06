#!/home1/amarrine/python/bin/python

import AlchemyDB, UnitType, User

adb = AlchemyDB.AlchemyDB()

u = UnitType.UnitType()
u.create_table(adb.engine)

u = User.User()
u.create_table(adb.engine)
