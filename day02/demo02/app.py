from flask import Flask
from werkzeug.routing import  BaseConverter
import config

app = Flask(__name__)
app.config.from_object(config)


class TelConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'

app.url_map.converters['tel'] = TelConverter

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
