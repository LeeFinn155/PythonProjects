import os

#
#       "Fake" Atomic Operations
#

#
# Get the current counter value
#
cfile = open("c:\\counter.txt")
counter = cfile.readline()
cfile.close()

# Use it
print("Currently", counter)

# Update it
cint = int(counter)
cint = cint + 1

counter = str(cint)

#
# ----
# Update it using an "atomic" style action
#


#
# Update the NEW version of the counter file with the new value
#

cfile = open("c:\\counter.txt", "w")
cfile.write(counter + "\n")
cfile.close()

# Delete the .old version before recreating it
if (os.path.exists("c:\\counter.old")):
    os.unlink("c:\\counter.old")
    
#Save the current version as .old just in case    
os.link("c:\\counter.txt","c:\\counter.old")

# Replace the new file
# FILE RENAME IS AN ATOMIC OPERATION
os.rename("c:\\counter.txt.new", "c:\\counter.txt")
