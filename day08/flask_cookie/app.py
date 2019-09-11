from flask import Flask,request,Response
from flask_script import  Manager
from datetime import datetime,timedelta
app = Flask(__name__)

manager = Manager(app)
app.config['SERVER_NAME'] =''
@app.route('/')
def hello_world():
    resp = Response("水浒传")
    # expires = datetime(year=2019,month=9,day=11,hour=9,minute=35)
    expires = datetime.now()+timedelta()
    resp.set_cookie("username","dahuangfeng",expires=expires,max_age=60)
    return resp

@app.route('/del/')
def delete_cookie():
    resp = Response("水浒传")
    reap =


if __name__ == '__main__':
    app.run()
