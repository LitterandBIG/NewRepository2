from flask import Flask,render_template
from flask_script import Manager
from flask_restful import Api,Resource,reqparse
app = Flask(__name__)
manager = Manager(app)
api = Api(app)

# class LoginView(Resource):
#     def post(self,username=None):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username')
#         return {"username":"chaoren"}

class LoginView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,help='用户名验证错误')
        args = parser.parse_args()
        print(args)
        return


api.add_resource(LoginView,'/login/<username>/','/signup/')

#注意事项
#如果想要返回json数据，就使用flask_restful 还有就是类试图
#class JsonView(view): def dispath_request(self):jsonify(self.get_data)
#如果想返回页面，那么 app.route 就可以了


@app.route('/')
def hello_world():
    return render_template('index.html')




if __name__ == '__main__':
    app.run()
