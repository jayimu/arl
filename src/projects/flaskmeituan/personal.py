#coding=utf-8
from common import  *
from pymysql import *
import json

connmysql=Query()
db=connmysql.conn()

@app.route("/topersonal")
def topersonal():
    return app.send_static_file('personal.htm')

