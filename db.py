# models.py
import time

from flask import Markup

from peewee import *

from app import db

class Document(Model):
    content = TextField()
    timestamp = IntegerField(default=int(time.time()))
    expired_timestamp = IntegerField(default=int(time.time()+ 20))
    title = TextField()
    key = TextField(index=True, unique=True)

    class Meta:
        database = db

    def html(self):
        return Markup(self.content)