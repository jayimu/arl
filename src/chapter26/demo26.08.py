from urllib3 import *
from bs4 import BeautifulSoup
disable_warnings()

html = '''
<html>
    <head><title>我的网页</title></head>
    <body attr="test" class = "style1">
    <a href='aa.html'>aa.html</a>
    <a href='bb.html' class = "style1">bb.html</a>
    <b>xyz</b>
    </body>
</html>
'''
soup = BeautifulSoup(html,"lxml")
from bs4 import NavigableString
def filterFun(tag):
    if tag.has_attr('class'):
        if 'style1' in tag['class']:
            return True
    return False

for tag in soup.find_all(filterFun):
    print(tag)
    print('------------')
