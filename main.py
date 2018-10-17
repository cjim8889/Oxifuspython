# main.py
from app import app
from db import Document
import views

if __name__ == '__main__':
    Document.create_table(True)
    app.run('0.0.0.0')