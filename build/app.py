"""
A small starter app to get Flask, Flask-RESTful and Flask-SQLAlchemy all talking.
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from build.config import DB_URI, DB_TRACK

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DB_TRACK
db = SQLAlchemy(app)
api = Api(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(128), unique=True)

    def __init__(self, first_name, last_name, email,
                 username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)

db.drop_all()
db.create_all()

user_e = User('Erik', 'Kvale', 'eirikval@gmail.com', 'eirikval', 'Gunnar14')
user_a = User('Amara', 'Faucett', 'amara@gmail.com', 'amaralady', 'swissbeauty')
db.session.add(user_e)
db.session.add(user_a)
db.session.commit()


class UserResource(Resource):

    def get(self):
        return {'Hello': 'world'}

api.add_resource(UserResource, '/user')


if __name__ == '__main__':
    app.run(debug=True)
