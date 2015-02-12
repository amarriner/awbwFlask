#!/usr/bin/env python

import AlchemyDB, CountryType

adb = AlchemyDB.AlchemyDB()

u = CountryType.CountryType()
u.create_table(adb.engine)
