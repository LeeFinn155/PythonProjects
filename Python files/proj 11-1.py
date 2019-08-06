# Process is a program + thread + multiple variables
import subprocess
import time

proc = subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

val = proc.poll()

while (val is None):
    print("Still running....")
    time.sleep(3)
    val = proc.poll()

print("Done.")
