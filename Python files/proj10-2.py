import datetime

now = datetime.datetime.now()

classend = datetime.datetime(2019, 5, 3)

time_until = classend - now

print("Only", time_until.days, "days until I no longer have to listen to Mark")
