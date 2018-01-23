from flask import Flask,session,redirect,url_for,request,make_response,jsonify
from datetime import datetime,timedelta
from pymysql import *
import json

app = Flask(__name__,static_url_path='/static')

class Query:
    def conn(self):
        db=connect("127.0.0.1","root","12345678","meituan",charset='utf8')
        return db







