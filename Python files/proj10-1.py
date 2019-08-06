import datetime

now = datetime.datetime.now()

print("Hour = ", now.hour, "Minutes = ", now.minute)

#Old-school way
minstr = str(now.minute)
if (len(minstr) < 2):
    minstr = "0" + minstr

#New-school way
minstr = str(now.minute).zfill(2)

#Newest-school way
hhmm = str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2)

print(hhmm)

#Or I can just let the system do it
hhmm = now.strftime("%I:%M")
print(hhmm)

#use help(time.strftime) in module to list commonly used format codes
longversion = now.strftime("%B %d, %Y at %I:%M")
print(longversion)


