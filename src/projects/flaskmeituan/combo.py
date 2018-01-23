from common import *
from random import *
query = Query()
db = query.conn()

@app.route('/tocombo/<shopId>/<comboId>')
def tocombo(shopId,comboId):
    return app.send_static_file('combo.htm')

@app.route('/combo',methods=['GET','POST'])
def combo():
    cursor = db.cursor()
    comboId = request.form.get('cid')
    sql = "select * from v_shop_combo where _id='%d'" % (int(comboId))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_id','combo_name','end_time','discount_cost','original_cost','combo_cover','shop_name','shop_cover','hits','address','current_cost','tel','time','sub_field_id','sub_field_name','sub_field_name','field_name']
        arr = []
        for row in results:
            time = str(row[3])
            d = dict(zip(fields,row))
            d['end_time'] = time
            arr.append(d)
        return json.dumps(arr)  
    except Exception as e:
        print(e)
    db.close();
#  获取套餐的详细内容
@app.route('/combo/content',methods=['GET','POST'])
def comboContent():
    cursor=db.cursor()
    comboId = request.form.get('cid')
    sql = "select * from t_sub_combo where combo_id = '%d'" % (int(comboId))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','combo_id','cname','product','price','amount','total']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))  
        return json.dumps(arr)        
    except Exception as e:
        print(e)
    db.close()        
    
# 获取店铺的推荐信息
@app.route('/combo/recommend',methods=['GET','POST'])
def recommend():
    cursor = db.cursor()
    shopId = request.form.get('sid')
    sql= "select * from v_shop_pic where type=2 and shop_id='%d'" % int(shopId)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_id','pic_url','type','shop_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))  
        return json.dumps(arr)          
    except Exception as e:
        print(e)
@app.route('/combo/shoppic',methods=['GET','POST'])
def shoppic():
    cursor = db.cursor()
    shopId = request.form.get('sid')
    sql = "select * from v_shop_pic where type=1 and shop_id='%d'" % int(shopId)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_id','pic_url','type','shop_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))  
        return json.dumps(arr)          
    except Exception as e:
        print(e)
        