import os
from flask import Flask
from flask_script import Manager
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
from flask_wtf import FlaskForm   #导入基类表单
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import SubmitField
from flask_bootstrap import Bootstrap
from PIL import Image
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ASFHOHOHKHHO'
app.config['MAX_CONTENT_LENGTH'] = 8*1024*1024   #自己设置文件的大小
#设置保存的位置
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.path.dirname(__file__),'uploads')
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
#创建文件上传对象，主要用来设置允许上传的类型
photos = UploadSet('photos',IMAGES)

#将上传对象跟app绑定
configure_uploads(app,photos)
#配置上传文件的大小，size默认64M，ruguo size为None，即按照设置的大小保存
patch_request_class(app,size= None)
bootstrap = Bootstrap(app)
manager =Manager(app)

#生成随机字符串
def random_string(length= 20):
    import random
    base_str = 'asdhfiehfoiweohfsdfhslfh'
    return ''.join(random.choice(base_str) for i in range(length))

#创建一个上传表单
class UploadForm(FlaskForm):
    photo = FileRequired('头像上传',validators=[])


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
