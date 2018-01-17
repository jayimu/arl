#coding:utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit,QLabel,QPushButton
from PyQt5.QtCore import QTimer
from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import DescribeDomainsRequest,DescribeDomainRecordsRequest,UpdateDomainRecordRequest
import json,urllib,re
from urllib3 import *
from asyncio.tasks import sleep
import time

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        self.lb=QLabel(self)
        self.lb.setText('当前IP')
        self.lb.move(50,22) 
        #获取当前ip  
        ip=GetLocalIP()    
        self.le = QLineEdit(self)
        self.le.setText(ip)
        self.le.resize(150,22)
        self.le.move(130, 26)
        #设置时间
        self.lbs=QLabel(self)
        self.lbs.setText('更新时间')
        self.lbs.move(50,52) 
        #获取当前ip  
        self.les = QLineEdit(self)
        self.les.setText('10')
        self.les.resize(150,22)
        self.les.move(130, 56)
        #提交按钮
        qbtn = QPushButton('执行', self)
        
        qbtn.clicked.connect(self.start)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 90)       
        #主体
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('获取当前ip')    
        self.show()
    def start(self):
        a=self.GETtext()
        t=int(a)*1000
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.setip)
        self.timer.start(t)
     
    def GETtext(self):
        a=self.les.text()
        return a   
        
    def setip(self):
        ip=GetLocalIP()
        self.le.setText(ip)
        UpdateIp()    

http = PoolManager()
#替换以下参数
ID="LTAIy4yiWlxjnF6c"
Secret="H4PwbOoVQeribfS7skuQPKq05wC88m"
RegionId="cn-hangzhou"
DomainName="jiketiku.cn"
#想要自动修改的主机名和域名类型
HostNameList = ['www','@']
Types = "A"

clt = client.AcsClient(ID,Secret,RegionId)

#获取公网ip
def GetLocalIP():
    IPInfo = http.request('GET',"http://ip.chinaz.com/getip.aspx")
    IPInfo=IPInfo.data.decode('utf-8')
    IPInfo=IPInfo.replace('b','')
    IPInfo=IPInfo.replace('ip','"ip"')
    IPInfo=IPInfo.replace('address','"address"')
    IPInfo=eval(IPInfo)
    IP = IPInfo['ip']
    return IP

#获取域名列表（暂时无用）
def GetDomainList():
    DomainList = DescribeDomainsRequest.DescribeDomainsRequest()
    DomainList.set_accept_format('json')
    DNSListJson = json.loads(clt.do_action_with_exception(DomainList))
    print (DNSListJson)

#更新域名ip
def EditDomainRecord(HostName, RecordId, Types, IP):
    try:
        UpdateDomainRecord = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
        UpdateDomainRecord.set_accept_format('json')
        UpdateDomainRecord.set_RecordId(RecordId)
        UpdateDomainRecord.set_RR(HostName)
        UpdateDomainRecord.set_Type(Types)
        UpdateDomainRecord.set_TTL('600')
        UpdateDomainRecord.set_Value(IP)
        UpdateDomainRecordJson = json.loads(clt.do_action_with_exception(UpdateDomainRecord))
        print (UpdateDomainRecordJson)
    except Exception as e:
        return e   

#获取域名信息
def GetAllDomainRecords(DomainName, Types, IP):
    DomainRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    DomainRecords.set_accept_format('json')
    DomainRecords.set_DomainName(DomainName)
    DomainRecordsJson = json.loads(clt.do_action_with_exception(DomainRecords))
    for HostName in HostNameList:
        for x in DomainRecordsJson['DomainRecords']['Record']:
            RR = x['RR']
            Type = x['Type']
            if RR == HostName and Type == Types:
                RecordId = x['RecordId']
                print (RecordId)
                EditDomainRecord(HostName, RecordId, Types, IP)

def UpdateIp():
    IP = GetLocalIP()
    print(IP)
    GetDomainList()
    GetAllDomainRecords(DomainName, Types, IP)
    
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

