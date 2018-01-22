from urllib import request  
import re  
from bs4 import BeautifulSoup  
from time import ctime,sleep
import os,sys,io
import threading
os.makedirs('urls', exist_ok = True)

insertUrl=["https://geekori.com"]

delUrl=[]

def getUrl():
    while(1):
        global insertUrl
        global delUrl  
        try:  
            if  len(insertUrl)>0 :  
                url = insertUrl[0]
                html = request.urlopen(url).read() 
                
                soup = BeautifulSoup(html,"lxml")
                
#                 write in file
                title=soup.find(name='title').get_text().replace('\n','')
                fp=open("./urls/"+str(title)+".html",'w',encoding='utf-8')
                fp.write(str(html.decode('utf-8')))
                fp.close()
                
                href_ = soup.find_all(name='a')
               
                for each in href_:
                    urlStr=each.get('href')  
                    if str(urlStr)[:4]=='http' and urlStr not in insertUrl:  
                       
                        insertUrl.append(urlStr)
                     
                        print(urlStr)                
                delUrl.append(insertUrl[0])
                del insertUrl[0]
        except:
            delUrl.append(insertUrl[0])
            del insertUrl[0]
            continue
        sleep(2)

threads = []
t1 = threading.Thread(target=getUrl)
threads.append(t1)
t2 = threading.Thread(target=getUrl)
threads.append(t2)
t3 = threading.Thread(target=getUrl)
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for tt in threads:
        tt.join()