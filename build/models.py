from datetime import datetime
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from build.app import db

# Model(s)
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(128), unique=True)
    models = db.relationship('Model', backref='curator', lazy='dynamic')

    def __init__(self, first_name, last_name, email,
                 username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pass_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)



class Model(db.Model):
    __tablename__ = 'model'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surface_area = db.Column(db.Float)
    volume = db.Column(db.Float)
    size_x = db.Column(db.Float)
    size_y = db.Column(db.Float)
    size_z = db.Column(db.Float)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, surface_area, volume,
                 size_x, size_y, size_z):
        self.name = name
        self.surface_area = surface_area
        self.volume = volume
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z

    def __repr__(self):
        return "<Model {}>".format(self.name)
