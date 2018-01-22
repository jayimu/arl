from urllib3 import *
from bs4 import BeautifulSoup
import re
disable_warnings()
http = PoolManager()
def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    
    headersText = f.read()

    headers = re.split('\n',headersText)
    n = 0
    for header in headers:
        result = header.split(':',maxsplit=1)
        headerDict[result[0]] = result[1] 
    f.close()
    return headerDict
headers = str2Headers('headers.txt')
#https://item.jd.com/12224904.html
r = http.request('GET','https://item.jd.com/12002469.html',headers = headers )
soup = BeautifulSoup(r.data,"lxml")

priceList = soup.find_all('ul',class_='p-parameter-list')
bookDetails1 = {}
for child in priceList[0].children:
    if child.name == 'li':  
        list = child.text.split('：')
        key = list[0].strip()
        value = list[1].strip()
        bookDetails1[key] = value

def filterFun(tag):
    if tag.name == 'li':
        if tag.parent.get('class') == ['p-parameter-list']:
            return True
    return False
bookDetails2 = {}
for tag in soup.find_all(filterFun):
    list = tag.text.split('：')
    key = list[0].strip()
    value = list[1].strip()
    bookDetails2[key] = value
print(bookDetails2)

