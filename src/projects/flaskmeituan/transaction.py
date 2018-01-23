from common import *
import random
import time
query = Query()
db = query.conn()

@app.route('/transaction',methods=['GET','POST'])
def transaction():
    cursor=db.cursor()
    userId= session['userid']
    
    transactionId = '20171112' + ''.join(random.sample('0123456789',5))
    session['trade_id'] = transactionId
    comboId = int(request.form.get('cid'))
    productName = request.form.get('cname')
    amount=int(request.form.get('q'))
    stime = time.time()
    etime = stime + 86400
    dcost = request.form.get('dcost')
    dcost1 = float(dcost)
    total = amount * dcost1
    sql="insert into t_trade_record (trasaction_id,combo_id,product_name,amount,user_id,start_time,end_time,total) values ('%s','%d','%s','%s','%d','%s','%s','%s')" %(transactionId,comboId,productName,amount,userId,stime,etime,total)
    try:
        cursor.execute(sql)
        db.commit()
        return redirect('/topay')
    except Exception as e:
        print(e)
    db.close()
    
# 获取订单信息
@app.route('/transaction/payment')
def payment():
    cursor = db.cursor()
    tid = session['trade_id']
    userId = session['userid']
    sql = "select * from v_shop_combo_trade where trasaction_id='%s' and user_id='%d'" % (tid,userId)
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        fields = ['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))  
        return json.dumps(arr)         
    except Exception as e:
        print(e)
    db.close()
@app.route('/update',methods=['GET','POST'])
def updata():
    cursor=db.cursor()
    tid=session['trade_id']
    userid=session['userid']
    print('up')
    sql="update t_trade_record  set yn=1 where trasaction_id='%s' and user_id='%d'" %(tid,userid)
    try:   
        cursor.execute(sql)
        db.commit()
        return "1"
    except Exception as e:
        return e
    db.close()

