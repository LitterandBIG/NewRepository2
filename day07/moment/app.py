from flask import Flask,render_template
from flask_moment import Moment
from flask_script import Manager,Time
from datetime import datetime
app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/moment/')
def moments():
    public_time
    return render_template('moment.html')



if __name__ == '__main__':
    app.run()
