import os

start = input("Enter starting point: ")

for (dirname, dirs, files) in os.walk(start):
    print(dirname)

    for f in files:
        print("...", f)
