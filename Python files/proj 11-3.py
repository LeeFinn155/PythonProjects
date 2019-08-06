import shelve

# Non-persistent dictionary, everytime i run the program i change the dictionary,
# everytime I close the program the dictionary gets erased
db = shelve.open(r"C:\Users\labuser\Desktop\simple-db.db")

db["key1"] = "value1"

key = input("Enter a new key           : ")
val = input("Enter a value for that key: ")

db[key] = val

for k in db.keys():
    print("Key", k,"=", db[k])

db.close()
