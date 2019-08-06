import datetime
import time


dt1 = datetime.datetime.now()
#.now() creates the date object from something similiar to now

time.sleep(10)

dt2 = datetime.datetime.now()

sleeptime = dt2 - dt1  # Should get something close to 10 seconds

onehourfromnow = dt2 + datetime.timedelta(hours=1)
