#    in CMD
#
#cd "\Python34\Scripts"
#pip3 install openpyxl

import openpyxl

filename = "C:\\Users\\labuser\\Desktop\\Four-Cells.xlsx"

workbook = openpyxl.load_workbook(filename)

sheet = workbook.get_sheet_by_name("Sheet1")

#in shell you can sheet["A1"].value to display the value in A1, for example.

for row in range(1,5):
    for col in range(1,5):
        print(row,col,sheet.cell(row,col).value)
