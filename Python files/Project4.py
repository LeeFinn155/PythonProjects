from bs4 import BeautifulSoup  # pip3 install bs4
import csv
import urllib.request
import requests

url_input = input("Enter URL: ")  # Asks User for URL
csv_input = input("Enter Output (CSV) filename: ")  # Ask User for CSV fielname

# Handle the exception
while True:
    try:
        num = (int(input("Enter Table # (positive integer): ")))
        if num > 0:
            num = num - 1
            break
    except ValueError:
        print("Please enter a positive integer")

url = url_input  # Saves url_input as the url variable
csv = (csv_input.encode('utf-8', 'ignore'))  # Saves csv_input as the csv variable
# ('utf-8', 'ignore') leaves the character out of Unicode result

fetch = requests.get(url)  # fetches the url
bs = BeautifulSoup(fetch.text, 'html.parser')  # parsing document into bs constructor

table = bs.select('table')[num]  # table variable, based on the table i want to find the tbody

tr_find = table.find_all('tr')  # finds the table row tag in the html document
columns = [x for x in tr_find[0].find_all('th')]

with open(csv, 'w') as output:  # opens csv for writing
    for i in range(1, len(tr_find)):  # iterates over tr in html file
        tds = tr_find[i].find_all('td')  # for the length of tr in table
        print('\n')  # Print a new line

        for j in range(len(tds)):  # iterates over td in html file
            values = [tds[j].text]  # changes list of table to text
            output.write(str(values))  # writes the value of the table selected to the csv file
