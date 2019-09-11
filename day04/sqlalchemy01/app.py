from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


class Person(object):
    name = 'xx'
    age = 18
    country = 'x'


p = Person('xx', 'xx')

if __name__ == '__main__':
    app.run()
