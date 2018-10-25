import json

from flask import session, make_response, Flask, request, render_template, send_from_directory
import os


app = Flask(__name__)
app.config.update(
    DEBUG=True,
)

@app.route('/static/<path>')
def statichandler(path):
    spath = os.path.abspath(os.path.dirname(__name__)) + "/templates"
    return send_from_directory(spath, path)


@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.secret_key = 'i-like-python-nmba'
    app.run()
