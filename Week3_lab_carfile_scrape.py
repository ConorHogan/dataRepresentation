"""week 3 webscraping lab"""

import requests
from bs4 import BeautifulSoup
import csv

# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page)
# print("------------------")
# print(page.content)
# soup1 = BeautifulSoup(page.content, 'html.parser')
# print("-------------------")
# print(soup1.prettify())

with open("D:\\Data_Analytics\\Data_repres\\Navigating_Dom\\Week2_Lab.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')
# print(soup.tr) # prints the first table row

# rows = soup.find_all("tr") # gets all the table rows
# for row in rows:
# 	print("-------")
# 	print(row)

# for row in rows:
# 	cols = row.find_all("td") # gets all the cell data
# 	datalist = []
# 	for col in cols:
# 		datalist.append(col.text)
# 	print(datalist)

employee_file = open('week02data.csv', mode='w', newline='')
employee_writer = csv.writer(employee_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

# employee_writer.writerow(['John Smith', 'Accounting', 'November'])
# employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

rows = soup.findAll("tr")
for row in rows:
    cols = row.findAll("td")
    datalist = []
    for col in cols:
        coldata = col.text
        if "Update" in coldata:
            continue
        elif "Delete" in coldata:
            continue
        else:
            datalist.append(col.text)
    employee_writer.writerow(datalist)
employee_file.close()




