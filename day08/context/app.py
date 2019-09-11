from flask import Flask, g, request, session, current_app, render_template
from utils import log_a, log_b, log_c

app = Flask(__name__)


@app.route('/')
def index():
    username = request.args.get('username')
    g.username = username
    log_a()
    log_b()
    log_c()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
