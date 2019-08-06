#Calculating change
#
#Write a program to calculate money, quarters, dimes, nickels and pennies
#

def printit(val,unit,units):
    if (val = 1):
        print(val, unit)
    elif (val > 0):
        print(val,unit,units)

def printit2(val,unit,units):
    if (val = 1):
        unit = units
    if (val > 0):
        print(val,unit)

cents = int(input("How many cents do you need? "))

quarters = cents // 25
cents    = cents %  25

dimes    = cents // 10
cents    = cents %  10

nickels  = cents // 5
cents    = cents % 5

pennies  = cents


print("You need:")
print("")

printit(quarters, "quarter", "quarters")
printit(dimes, "dime",       "dimes")
printit(nickels, "nickel",   "nickels")
printit(pennies, "penny",    "pennies")



