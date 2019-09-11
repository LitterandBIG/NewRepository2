from flask import Flask,render_template,request,send_from_directory,url_for
import os
from flask_script import Manager
#处理图片 要装上一个库 pillow 才能导入image库
from PIL import Image
app = Flask(__name__)
#设置允许的后缀
ALLOWED_EXTENSIONS = set(['png','ipg','jpeg'])
#设置保存的位置
app.config['UPLOAD_FOLDER'] = os.getcwd()
#设置文件上传的大小
app.config['MAX_CONTENT_LENGTH'] = 8*1024*1024
manager = Manager(app)

#判断是否是允许的后缀
def allowed(filename):
    return '.'in filename and filename.rsplit('.',1)[1] in  ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return 'Hello World!'
#http://127.0.0.1:5001/uploaded/CISSDERG.png/  让图片能访问，才能渲染发哦页面
@app.route('/uploaded/<filename>/')
def uploaded(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.('/upload/',methods=['POST','GET'])
def upload():
    img_url = None
    #获取表单提交的文件
    #保存上传的文件
    file = request.files.get('photo')  #接收表单提交的文件
    #print(file.filename)  输入文件的名字
    if file and allowed(file.filename):
        #获取文件后缀
        suffix =

if __name__ == '__main__':
    app.run()
