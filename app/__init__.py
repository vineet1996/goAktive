from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/proj'
db = SQLAlchemy(app)


class links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100))

from app import routes
