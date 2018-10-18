from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv

html_page = urlopen("https://www.cse.iitb.ac.in/page222")
soup = BeautifulSoup(html_page, "lxml")
links = []
Category = []

for link in soup.findAll('a', attrs = {'href': re.compile("^[?]batch")}):
    links.append(link.get('href'))
    Category.append(link.string)

main_link = []

size = len(links)

for i in range(size):
    main_link.append( "https://www.cse.iitb.ac.in/page222" + links[i])

html = []

for i in range(size):
    html.append(urlopen(main_link[i]))

Soups = []

for i in range(size):
    Soups.append(BeautifulSoup(html[i], "lxml"))

Total_link = []

for i in range(size):
    Total_link.append([])

for i in range(size):
    for link in Soups[i].find_all('a'):
        Total_link[i].append(link.string)

number = []

for i in range(size):
    count = 0
    j = 0
    while j < len(Total_link[i]) :
        if Total_link[i][j] == "Update":
            count = count + 1
        j = j + 1
    number.append(count)

with open('count.csv','w') as outcsv:
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(["Category Name", "No. of students"])
    for i in range(size):
        writer.writerow([Category[i], number[i]])
