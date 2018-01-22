from flask import *
import json
import pymysql
app =Flask(__name__)
def mysqlConnect(sql):
    db = pymysql.connect('localhost','root','12345678','weather',charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    data = json.dumps(data)
    db.close()
    #print(data)
    return data
    
@app.route('/weather')
def index():
    cityName = request.values.get('city')
    sql = "select * from t_weather where cityName like '%" +  cityName + "%' or cityNameen like '%" + cityName + "%'"    
    info = mysqlConnect(sql)
    return info

if __name__ == '__main__':
    app.run()