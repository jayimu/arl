from common import *
from random import *
query = Query()
db = query.conn()

@app.route('/toshop/<id>')
def toshop(id):
    return app.send_static_file('shop.htm')

@app.route('/shop',methods=['GET','POST'])
def shop():
    cursor = db.cursor()
    shopId = request.form.get('sid')
    sql = "select * from v_shop_fields where _id='%d'" %(int(shopId))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        
        fields = ['_id', 'shop_name','shop_cover','hits','address',
                  'd_id','current_cost','tel','time','field_id','sub_field_id',
                  'field_name','sub_field_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))
        return json.dumps(arr)                
    except Exception as e:
        return e
    db.close()

# 获取店铺的套餐信息
@app.route('/shop/combo',methods=['GET','POST'])
def shop_combo():
    cursor = db.cursor()
    shopId = request.form.get('sid')
    sql = "select * from t_shop_combo where shop_id='%d'" % (int(shopId))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id', 'shop_id','combo_name','end_time','discount_cost','original_cost',
                  'combo_cover']
        arr = []
        for row in results:
            time = str(row[3])
            d = dict(zip(fields,row))
            d['end_time'] = time
            arr.append(d)
        return json.dumps(arr)         
    except Exception as e:
        return e
    db.close()
# 获取店铺的评论信息
@app.route('/shop/discuss',methods=['GET','POST'])
def shop_discuss():
    cursor = db.cursor()
    shopId = request.form.get('sid')
    sql = "select * from v_user_discuss where shop_id='%d'" % (int(shopId))
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','user_id','shop_id','discuss','classify_id','discuss_time','nickname','user_pic','classify_name','shop_name']
        arr = []
        for row in results:
            time = str(row[5])
            d = dict(zip(fields,row))
            d['discuss_time'] = time
            arr.append(d)
        return json.dumps(arr)           
    except Exception as e:
        print(e)
        return e
    db.close()