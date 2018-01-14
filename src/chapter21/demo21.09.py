# Jinja2模板的过滤器
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('filter.txt',name='bill',value='I love python.')
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')