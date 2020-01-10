import requests
import xlwt

from bs4 import BeautifulSoup
from selenium import webdriver

#website where we get our source data
url = "http://worldpopulationreview.com/states/"

#set up 
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#will find columns of table with these specific tags: These r the titles
columns = soup.find_all('a', style= "color:black;cursor:pointer;display:inline-block")

#the entire table
table = soup.find("table", class_ = "table-striped")

#create excel work book to be used in Tableau
workbook = xlwt.Workbook()
data = workbook.add_sheet("US Population Data")
rowNum = 0
col = 0

#tr is the tag for every row

for row in table.select('tr'):
    #td is each indiviual value in the row
    tds = row.find_all('td')
    line =""
    valueList =[]
    for value in tds:
      valueList.append(value.text)
    if valueList[2].isdigit():
      valueList[2] = int(valueList[2])
    data.write(rowNum, col, valueList[1])
    data.write(rowNum,col + 1, valueList[2])
    print("%2s %25s %15s" % (valueList[0],valueList[1],valueList[2]))
    rowNum += 1
workbook.save('US Population Data.xls')
