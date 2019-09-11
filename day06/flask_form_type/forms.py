from wtforms import Form, StringField, PasswordField, SubmitField,IntegerField,BooleanField,SelectField,DateField
from wtforms.validators import Length, EqualTo,Email,InputRequired,NumberRange,Regexp,URL,UUID
from flask_wtf import  FlaskForm
from wtforms import ValidationError

class RegisterForm(Form):
    username = StringField(validators=Length[(min=6,max=20,message='用户名长度在6-20位')])
    password = PasswordField(validators=[min = 6, max = 20, message = '用户名长度在6-20位']
