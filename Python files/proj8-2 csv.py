import csv

csvfile = open("C:\\Users\\labuser\\Desktop\\Four-Cells1.csv")

csvreader = csv.reader(csvfile)

data = list(csvreader)

#now data[1] in shell prints a row
#data[0][0] will print a cell

for row in range(0,len(data)):
   for col in range(0,len(data[row])):
        print(row,col,data[row][col])
    
