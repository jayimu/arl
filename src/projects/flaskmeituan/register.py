from common import *
from random import *
query = Query()
db = query.conn()

@app.route('/toregister')
def toregister():
    return app.send_static_file('register.htm')

@app.route('/register',methods=['GET','POST'])
def register():
    cursor = db.cursor()
    user = request.form.get('mobile')
    pwd = request.form.get('password')
    nickname = random_str()
    sql  = "insert into t_users(tel_number,nickname,password) value('%s','%s','%s')" % (user,nickname,pwd)
    try:
        cursor.execute(sql)
        db.commit()
        return redirect('/tologin')
    except:
        db.rollback()
    db.close()
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str