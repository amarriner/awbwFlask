#!/home1/amarrine/python/bin/python

import AlchemyDB, UnitType

adb = AlchemyDB.AlchemyDB()

u = UnitType.UnitType()
u.create_table(adb.engine)

