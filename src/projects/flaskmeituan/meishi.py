# coding = utf-8

from common import *
query = Query()
db = query.conn()

@app.route('/food')
def food():
    return app.send_static_file('meishi.htm')

@app.route('/district', methods=['GET','POST'])
def district():
    cursor = db.cursor()
    sql = 'select * from areas where cityid=210100 order by id asc'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id', 'areaid','area','cityid']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))
        return json.dumps(arr)      
    except Exception as e:
        return e
    db.close()
@app.route('/meishi/shop', methods=['GET','POST'])
def meishiShop():
    cursor = db.cursor()
    sql = 'select * from v_shop_fields where field_id = 1 order by _id asc'
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
# 返回指定美食分类的店铺
@app.route('/meishi/click',methods=['GET','POST'])
def subclick():
    cursor = db.cursor()
    subId = request.form.get('sub_id')
    sql = "select * from v_shop_fields where sub_field_id='%d' order by _id asc" % (int(subId))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_name','shop_cover','hits','address','d_id','current_cost','tel','time','field_id','sub_field_id','field_name','sub_field_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))
        return json.dumps(arr)   
    except Exception as e:
        return e
    db.close()   
@app.route('/district/click',methods = ['GET','POST'])
def disclick():
    cursor = db.cursor()
    areaId = request.form.get('area_id')
    sql = "select * from v_shop_fields where d_id='%d' order by _id asc" % (int(areaId))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_name','shop_cover','hits','address','d_id','current_cost','tel','time','field_id','sub_field_id','field_name','sub_field_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))
        return json.dumps(arr)   
    except Exception as e:
        return e
    db.close()   
@app.route('/meishi/up',methods = ['GET','POST'])
def up():
    cursor = db.cursor()
   
    sql = "select * from v_shop_fields  order by current_cost asc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_name','shop_cover','hits','address','d_id','current_cost','tel','time','field_id','sub_field_id','field_name','sub_field_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))
        return json.dumps(arr)   
    except Exception as e:
        return e
    db.close()   
@app.route('/meishi/down',methods = ['GET','POST'])
def down():
    cursor = db.cursor()
   
    sql = "select * from v_shop_fields  order by current_cost desc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_name','shop_cover','hits','address','d_id','current_cost','tel','time','field_id','sub_field_id','field_name','sub_field_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))
        return json.dumps(arr)   
    except Exception as e:
        return e
    db.close()   