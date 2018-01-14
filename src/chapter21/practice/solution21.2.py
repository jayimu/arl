from flask import Flask
app = Flask('__name__')
@app.route('/test/<a1>:<a2>:<a3>')
def test(a1,a2,a3):
    return '<h1>%s.%s.%s</h1>' %(a1,a2,a3)

if __name__ == '__main__':
    app.run()