import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

table = soup.findAll('table')[0]

list_of_rows = []
for row in table.findAll('tr')
    list_of_cells = []
    for cell in row.findAll('td'):[1] 
        list_of_cells.append(cell.text)
        if cell.find('a'):
            list_of_cells.append('http://www.tdcj.state.tx.us/death_row/dr_info/' + cell.find('a')['href'])
    list_of_rows.append(list_of_cells)
    
outfile = open('./releases.csv', 'wb')
writer = csv.writer(outfile)
writer.writerow(['scheduled execution', 'link', 'last name', 'first name', 'TDCJ number', 'date of birth', 'race', 'date received', 'county'])
writer.writerows(list_of_rows)