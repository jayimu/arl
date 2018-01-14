from flask import Flask,request,render_template
from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField,validators
app = Flask(__name__)
app.secret_key ='sdjsldj4323sdsdfssfdf43434'

class ContactForm(FlaskForm):
    firstname = TextField('姓名',[validators.Required('姓名必须输入')])
    submit = SubmitField('提交')
@app.route('/', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print(form.firstname.errors)
            print('error')
    return render_template('first.txt',form=form)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')


