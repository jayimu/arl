from flask import Flask
from time import *
app = Flask(__name__)
@app.route('/')
def hello():
    return strftime('%Y-%m-%d %H:%M:%S',localtime(time()))
if __name__ == "__main__":
    app.run()
