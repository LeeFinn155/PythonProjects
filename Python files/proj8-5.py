import time

before = time.time()

for i in range(0,2000000):
    pass

after = time.time()

print("That took", after-before, "seconds")
