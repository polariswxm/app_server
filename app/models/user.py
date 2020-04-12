from app.extensions import db, login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER,primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(128))

    # add relationship model
    posts = db.relationship('Posts', backref='user', lazy='dynamic')


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))



