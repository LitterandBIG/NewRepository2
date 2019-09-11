import os
from flask import Flask
from flask_mail import Message,Mail
app = Flask(__name__)


app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.qq.com')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_SERVER','smtp.qq.com')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
