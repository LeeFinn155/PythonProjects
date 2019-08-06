
#   A simple program to test various regular expression patterns 

import re

pattern = input("Enter pattern: ")
teststr = input("Enter a string to test: ")

# 2-step method:
#
# p = re.compile(pattern)
# m = p.search(teststr) 

# 1-step method:

m = re.search(pattern, teststr)

if (m is None):
    print("No match")
else:
    print("Match")
    print("Matched string = ", m.group(0))

    for s in m.groups():
        print("=>", s)

