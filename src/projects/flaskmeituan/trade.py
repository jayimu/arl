#coding=utf-8
from common import  *
from pymysql import *
import json

connmysql=Query()
db=connmysql.conn()

@app.route("/totrade")
def tra():
    return app.send_static_file('trade.htm')

@app.route('/trade',methods=['GET','POST'])
def trade():
    cursor=db.cursor()
    id=session['userid']
    sql="select * from v_shop_combo_trade where user_id=%d" %(id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        par=['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr=[]
        for row in results:
            arr.append(dict(zip(par,row)))
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()

@app.route('/trade/paid',methods=['GET','POST'])
def paid():
    cursor=db.cursor()
    id=session['userid']
    sql="select * from v_shop_combo_trade where yn=1 and user_id=%d" %(id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        par=['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr=[]
        for row in results:
            arr.append(dict(zip(par,row)))
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()
    
@app.route('/trade/non-payment',methods=['GET','POST'])
def nopayment():
    cursor=db.cursor()
    id=session['userid']
    sql="select * from v_shop_combo_trade where yn=0 and user_id=%d" %(id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        par=['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr=[]
        for row in results:
            arr.append(dict(zip(par,row)))
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()
    

@app.route("/totinfo/<tid>")
def toinfo(tid):
    return app.send_static_file('trade_info.htm')
    

@app.route('/tradeinfo',methods=['GET','POST'])
def tinfo():
    cursor=db.cursor()
    tid=request.form.get('tid')
    id=session['userid']
    sql="select * from v_shop_combo_trade where trasaction_id=%s and user_id=%d" %(tid,id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        par=['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr=[]
        for row in results:
            arr.append(dict(zip(par,row)))
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()  