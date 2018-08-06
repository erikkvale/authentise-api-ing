from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from .app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(200))
    username = db.Column(db.String(200))
    password = db.Column(db.String(128))
    models = db.relationship('Model', backref='maker', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "User {}".format(self.username)


class Model(db.Model):
    __tablename__ = 'model'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    size_x = db.Column(db.Float)
    size_y = db.Column(db.Float)
    size_z = db.Column(db.Float)
    surface_area = db.Column(db.Float)
    volume = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "Model: {}".format(self.name)
