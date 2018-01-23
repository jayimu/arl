#coding=utf-8
from common import *
import meishi
import register
import login
import shop
import combo
import transaction
import pay
import account
import personal
import trade
app.secret_key = '\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'

query = Query()
db = query.conn()
@app.route('/')
def first():
    return app.send_static_file('index.htm')

@app.route('/field')
def index_fields():
    cursor = db.cursor()
    sql = 'select * from t_fields where flag = 1 order by order_value asc'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        fields = ['_id', 'field_name','order_value','flag']
        arr = []        
        for row in results:
            arr.append(dict(zip(fields,row)))
        return json.dumps(arr)
      
    except Exception as e:
        return e
    db.close()
    
@app.route('/sub_field',methods=['GET','POST'])
def sub_fields():
    cursor = db.cursor()
    sql = 'select * from t_sub_fields where field_id = 1 and flag = 1 order by order_value asc'
    fid = request.form.get('fid')
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id', 'sub_field_name','field_id','order_value','flag']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))
        return json.dumps(arr)        
    except Exception as e:
        return e
    db.close()

@app.route('/islogin')
def session1():
    if 'username' in session:
        print(session['nickname'])
        return session['nickname']
    return '未登录'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234)