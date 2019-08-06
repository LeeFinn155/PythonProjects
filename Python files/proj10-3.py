import datetime

in_str = input("Enter a date: ")
fmt = "%m/%d/%y"

then = datetime.datetime.strptime(in_str,fmt)

now = datetime.datetime.now()

time_until = then - now

print("That is",time_until.days, "days to go")

# OR USE DATEUTIL (pip3 install py-dateutil) TO HANDLE "many" FORMATS

import dateutil.parser

in_str = input("Enter a date: (multiple formats): ")
then = dateutil.parser.parse(in_str)

time_until = then - now
print("That is",time_until.days, "days to go")
