from datetime import datetime

from app.extensions import db


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, index=True, default=0)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # Join "users" table
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))


