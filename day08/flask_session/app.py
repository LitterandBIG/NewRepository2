from flask import Flask, session
from flask_script import Manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ADHFASDFLASKGK'
manager = Manager(app)


@app.route('/')
def index():
    # 当用户提交用户名和密码 验证成功后
    # 就将用户名和密码存入session
    session['username'] = 'rock'
    session['user_id'] = '9523'
    print(type(session))
    return 'Hello World!'


@app.route('/get_session/')
def get_session():
    username = session['username']
    user_id = session['user_id']
    print(username, user_id)
    return username or '没有任何的session'


@app.route('/del_session/')
def del_session():
    session.clear()
    return '退出成功'


if __name__ == '__main__':
    app.run()
