import tarfile

filename = input("Enter a TAR filename: ")

if (filename.endswith(".gz")):
    mode = "r:gz"
else:
    mode = "r"

tf = tarfile.open(filename, mode)

print("Here are the files within the TAR file")

for f in tf.getnames():
    print("...",f)

innername = input("Enter name of a single file within the TAR file: ")

f = tf.edxtractfile(innername)

# Can continue with using f.readline(), f.read(), etc.
