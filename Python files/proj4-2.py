import re

# Ask the user for a filename

fname = input("Enter a test string: ")

# Read the entire file
f = open(fname)
s = f.read()
f.close()

pattern = "((U\.?S\.?M\.?)|(U\s* of Southern Maine))"

newstr = re.sub(pattern, "University of Maine at Portland", teststr, flags=re.IGNORECASE)

if (s == newstr):
    print("No change necessary")
else:
    print("Creating new version...")

    f = open(fname + ".new", "w")
    f.write(newstr)
    f.close()
