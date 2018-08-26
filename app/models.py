from app import db

class links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100))
