#coding=utf-8
from common import  *
from pymysql import *
import json

connmysql=Query()
db=connmysql.conn()

@app.route("/toaccount")
def toaccount():
    return app.send_static_file('account.htm')

@app.route('/account',methods=['GET','POST'])
def account():
    cursor=db.cursor()
    id=session['userid']
    sql="select * from t_users where _id=%d" %(id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        fields=['_id','tel_number','nickname','password','user_pic']
        arr=[]
        for row in results:
            arr.append(dict(zip(fields,row)))
        print(arr)
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()

@app.route('/account/nickname',methods=['GET','POST'])
def nickname():
    cursor=db.cursor()
    id=session['userid']
    nick=request.form.get('username')
    sql="update t_users set nickname='%s' where _id='%d'" %(nick,id)
    print(nick)
    try:   
        cursor.execute(sql)
        session['nickname'] = nick
        return "1"
        
    except Exception as e:
        print(e)
        return "123"
    db.close()

@app.route('/account/password',methods=['GET','POST'])
def password():
    cursor=db.cursor()
    id=session['userid']
    pwd=request.form.get('password')
    sql="update t_users set password='%s' where _id='%d'" %(pwd,id)
    print(sql)
    try:   
        cursor.execute(sql)
        
        return "1"
        
    except Exception as e:
        print(e)
        return "123"
    db.close()















