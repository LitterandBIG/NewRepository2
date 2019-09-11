from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)

app.config['SECRET_KEY'] = 'KHLGDGJLDNFHO'



class RegisterForm(FlaskForm):
    name = StringField("用户名:",validators=[DataRequired])
    submit =SubmitField("立即注册",)





@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/',methods==['POST','GET'])
def register():
    name = None
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        print(name)
        form.name.data = ''
    return render_template('index.html',form=form,name=name)



if __name__ == '__main__':
    app.run()
