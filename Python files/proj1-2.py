#
#   Your name in lights
#
# ************************
# *      Lee Finn        *
# ************************
#
#  We'll make the box 60 chars

linelen = 60
name = input("What is your name? ")

if (len(name) > 56):
    linelen = len(name) + 4

#
#-----Line 1-------------
#


line1 = "*" * linelen
print(line1)

#
#-----Line 2-------------
#


blanks = linelen - 2 - len(name)  # Determine the num of spaces for the middle line
extra = len(name) % 2    # See if the name is odd
halfblanks = int(blanks/2)

spacesbefore = " " * halfblanks
spacesafter = " " * (halfblanks + extra) # Add an extra space afterwars if the name is odd

line2 = "*" + spacesbefore + name + spacesafter + "*"
 
print(line2)


#
#-----Line 3-------------
#

line3 = "*" * linelen
print(line3)
