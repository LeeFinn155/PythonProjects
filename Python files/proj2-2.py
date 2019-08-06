a = input("First number: ")
b = input("Second number: ")

try:
    a = int(a)
    b = int(b)
    ok = False
    
except ValueError:
    ok = True
    
print(a, "divided by",b,"=",a/b)

if (ok):
    if (b != 0):
        print(a, "divided by",b,"=",a/b)
    else:
        print("You can't divide by zero")
else:
    print("Please enter integer numbers")
