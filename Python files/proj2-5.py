portuguese = { "where" : "onde", "yes" : "sim" , "when" : "quando" }

engword = input("Enter an English word: ")

while(engword != ""):
    if (engword in portuguese.keys()):
        print(engword,"in Portuguese is", portuguese[engword])
    else:
        print("Sorry, I don't know how to say ",engword,"in Portuguese.")
        
    engword = input("Enter an English word: ")        

