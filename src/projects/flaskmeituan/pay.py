from common import *
from WXPay import *
import time
import random
import string
import urllib.parse
query = Query()
db = query.conn()

@app.route('/topay')
def topay():
    return app.send_static_file('pay.htm')
def createNonceStr(self):
    nonceStr = ''.join(random.sample(string.ascii_letters + string.digits,16))
    return nonceStr
def createId():
    a1 = int(time.time * 2)
    a2 = random.randint(0,10)
    a = '%d%d' % (a1,a2)
    return a
@app.route('/pay',methods=['GET','POST'])
def createOrder():
    name = urllib.parse.unquote(request.form.get('cname'))
    total = float(request.form.get('total')) * 100
    transaction_id = request.form.get('trade')
    nonce_str = createNonceStr()
    out_trade_no = createId()
    session['out_trade_no'] = out_trade_no
    
    requestData = {"body":'%s' %(name),
                   "out_trade_no":'%s' %(out_trade_no),
                   "total_fee":total,
                   "nonce_str":'%s' %(nonce_str),
                   "spbill_create_ip":'127.0.0.1',
                   "notify_url":'http://127.0.0.1/notify',
                   "trade_type":'NATIVE', # 扫码支付 ISAPI（公众号支付，需要使用证书文件）
                   "product_id":'%s' %(transaction_id),
                   "appid":'请输入公众号（服务号）的appid',
                   "mch_id":'请输入商户号'}
    wx = WXPay(requestData)
    orderResult = wx.createOrder()
    return redirect(url_for('toqr',_anchor = orderResult['code_url']))
@app.route('/toqr')
def toqr():
    return app.send_static_file('qr.htm')

@app.route('/pay/order', methods=['GET','POST'])
def queryOrder():
    nonce_str = createNonceStr()
    out_trade_no = session['out_trade_no']
    requestData = {"appid":'请输入公众号的AppID',
                   "mch_id":'请输入商户号',
                   "nonce_str":'%s' %(nonce_str),
                   "out_trade_no":'%s' %(out_trade_no)}
    wx = WXPay(requestData)
    queryResult = wx.queryOrder()
    state = queryResult['trade_state']
    return state