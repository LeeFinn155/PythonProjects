import json

js = json.loads('{ "a" : "b", "c" : "d" }')
print(type(js))

i = "-------"


print(i)

js2 = json.loads('[1, 2, 3, 5, 7, 9]')
print(type(js2))

print(i)

# Make a dictionary
python1 = { "key1" : "val1", "key2" : "val2", "key3" : 333 }
s = json.dumps(python1)
print(s)

print(i)

# Make a list
python2 = [2, 4, 6, 8, "hi mom", 10]
s = json.dumps(python2)
print(s)

print(i)

f = open(r"C:\Users\labuser\Desktop\json8-1.txt")

bigobj = json.load(f)

print(type(bigobj))
