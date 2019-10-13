"""lab_3 scraping from myhome.ie"""

import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://myhome.ie/residential/mayo/property-for-sale?page=1")

soup = BeautifulSoup(page.content, 'html.parser')
home_file = open('week03MyHome.csv', mode='w', newline='')
home_writer = csv.writer(home_file, delimiter='\t',quotechar='"', quoting=csv.QUOTE_MINIMAL)
# listings = soup.find("div", class_="PropertyListingCard")
# print(listings)
# # print(soup.prettify())

# price = listings.find(class_="PropertyListingCard__Price").text

# print(price)

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entryList = []
    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)
    # print(entry)
    home_writer.writerow(entryList)

home_file.close()






