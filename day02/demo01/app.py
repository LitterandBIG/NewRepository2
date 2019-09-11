from flask import Flask
from werkzeug.routing import BaseConverter
import config

app = Flask(__name__)
app.config.from_object(config)


class TelConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


app.url_map.converters['tel'] = TelConverter

@app.route('/tel/<tel:number>/')
def tel(number):
    return number


@app.route('/uuiddemo/<uuid:u_id>/')
def hello_world(u_id):
    return 'Hello World! 我是1234567 %s' % u_id



if __name__ == '__main__':
    app.run()
