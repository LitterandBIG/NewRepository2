from flask import Flask, request, render_template
from flask import RegisterForm, LoginFORM
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hljljlljk'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register/', methods=['PORT', 'GET'])
def register():
    form = RegisterForm()
    if request.method == "GET":
        return render_template('register.html', form=form)
    else:
        form = RegisterForm(request.form)  # 表单提交过来的内容作为参数
        if form.validate():  # 如果用户的输入满足要求
            return 'success'
        else:
            print(form.errors)  # 打印表单错误信息
            return 'fail'


@app.route('/login/', methods=['PORT', 'GET'])
def login():
    if request.method == "GET":
        return render_template('login.html', form=form)
    else:
        form = LoginFORM(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
