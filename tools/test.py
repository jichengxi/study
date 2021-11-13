import datetime

from dateutil.tz import tzutc, tzlocal

a = datetime.datetime(2021, 9, 10, 6, 52, 31, tzinfo=tzutc())

print(datetime.tzinfo())
print(type(a))
