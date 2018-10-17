# views.py
from flask import abort, request
from flask import render_template
import time
from app import app
from db import Document
import json
from hash import key

@app.route('/<key>', methods=['GET', 'POST'])
def Page(key):
    try:
        content = Document.get(Document.key == key)
    except Document.DoesNotExist:
        abort(404)
    if content.expired_timestamp < int(time.time()):
        content.delete_instance()
        abort(404)
    else:
        return render_template('page.html',content=content.html(), endtime=content.expired_timestamp, title= content.title)

@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/publish', methods=['POST'])
def Publish():
    if request.form:
        recieved = request.form
        print(recieved)
        if recieved['content'] != '':
            content = recieved['content']
            title = recieved['title']
            length = int(recieved['length']) * 60
            expired_timestamp = int(time.time()) + length
            id = key()
            try:
                Document.create(content=content, expired_timestamp=expired_timestamp, key = id, title=title)
            except Exception:
                abort(500)

            link = 'https://oxifus.com/' + id
            ret = {'link': link}
            ret = json.dumps(ret)
            return ret

    abort(404)