import threading
import time

def thread1():
    print("Thread 1 start")
    time.sleep(10)
    print("Thread 1 stop")

def thread2():
    print("Thread 2 start")
    time.sleep(5)
    print("Thread 2 cont")
    time.sleep(10)
    print("Thread 2 stop")


# Single threaded version
thread1()
thread2()

print("-" * 40)

# Multi-threaded version

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()
