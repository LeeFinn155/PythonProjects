import re
#Find things that in the form 3 letters an optional space and number

s = input("Enter a line to check: ")
#pattern = "[A-Z][A-Z][A-Z] [1-90]+"    #Cleaning up
#pattern = "[A-Z]{3} \d+"               #Further cleaning up
#pattern = "[A-Z]{3} \d{1,4}"           #And more
pattern = "\s([A-Z]{3}\s?\d{1,4})\s" 

#Do the regular expression search
m = re.search(pattern,s)

#See if we found anything
if (m is not None):
    found = m.group(0)

    print(found)
    
else:
    print("Nothing was found")
