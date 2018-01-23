from common import *
from random import *
query = Query()
db = query.conn()

@app.route('/tologin')
def tologin():
    return app.send_static_file('login.htm')

@app.route('/login',methods=['GET','POST'])
def login():
    cursor = db.cursor()
    user = request.form.get('email')
    pwd = request.form.get('password')
    sql = "select * from t_users where tel_number='%s' and password='%s'" % (user,pwd)
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        count = cursor.rowcount
        if count > 0:
            nickname = results[2]
            username = results[1]
            userid = results[0]
            session['username'] = username
            session['nickname'] = nickname
            session['userid'] = userid
            session.permanent = True
        return redirect('/')
    except Exception as e:
        return e
    db.close()    