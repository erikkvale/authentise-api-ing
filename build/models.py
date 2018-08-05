from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from .app import db


class User(db.Model):
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(200))
    username = db.Column(db.String(200))
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "User {}".format(self.username)

