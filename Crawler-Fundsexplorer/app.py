import csv
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup


# Data Cleansing
# 'R$' => '' | '%' => '' | '.0' => '' | '.' => '' | ',' => '.' | 'N/A' => ''

url_fundsexplorer = 'https://www.fundsexplorer.com.br/ranking'
print("Scraping data...{}".format(datetime.now()))

response = requests.get(url_fundsexplorer)
soup = BeautifulSoup(response.text, "html.parser")

data = []

table = soup.find(id="table-ranking")
table_head = table.find('thead')
rows = table_head.find_all('tr')

for row in rows:
    cols = row.find_all('th')
    colsd = [element.get_text(separator=" ").strip() for element in cols]
    data.append([e for e in colsd])

table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    colsd = [element.text.replace('R$','').replace('%','').replace('.0','').replace('.','').replace('N/A','').replace(',','.').strip() for element in cols]
    data.append([element for element in colsd])

file = open("fii.csv", "w")

wtr = csv.writer(file, delimiter=';', lineterminator='\n')
for x in data : wtr.writerow(x)

file.close()

print("Finish...{}".format(datetime.now()))

time.sleep(1)