import subprocess

# standardinput
#    Linux/Windows:
#    <
# standardoutput
#    Linux/Windows:
#    >  - overwrites
#    >> - always appends to the file
#
#    | (pipe) - takes the standardout of one program and links it to be the
#    standardin of another program

# stderr



# If want a program with arguments, pass it as an array
# (bottom) - only run command may be used on a module in Py 3.5
# proc = subprocess.run(["dir","c:\\Windows"], shell=True, stdout=subprocess.PIPE)
proc = subprocess.Popen(["dir","c:\\Windows"], shell=True, stdout=subprocess.PIPE)

for s in proc.stdout:
    s = s.decode('utf-8')   # Convert from bytes() to str()
    s = s.rstrip()          # Remove whitespace at the end-of-line
    
    print(">>>",s)
