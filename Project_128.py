import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)
soup = bs(page.text, "html.parser")

table = soup.find("table", attrs = {"class", "wikitable sortable jquery-tablesorter"})
temp_list = []
print(table)

for i in table:
    rows = i.find_all("tr")
    
for tr in rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td] #gives the value of one cell
    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns = ["star_names", "distance", "mass", "radius"])
df.to_csv("dwarf_stars.csv")