from app.extensions import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room = db.Column(db.String(100))
    desc = db.Column(db.String(255))
    time = db.Column(db.String(100))