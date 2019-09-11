from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context ={
        'ps':'<script>alert("test")<>'
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
