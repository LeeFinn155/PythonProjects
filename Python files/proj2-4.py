def method1():
    infile = open(r"c:\Users\labuser\Desktop\threelines.txt", "r")

    # Read all in a single step
    s = infile.read()
    print(s, end="")

    infile.close()

def method2():
    infile = open("c:\\Users\\labuser\\Desktop\\threelines.txt", "r")

    s = infile.readline()
    print(s, end="")

    s = infile.readline()
    print(s, end="")

    infile.close()

def method3():
   infile = open("c:\\Users\\labuser\\Desktop\\threelines.txt")


   for s in infile:
        print(s, end="")
        


   infile.close()
    
