"""
A small starter app to get Flask, Flask-RESTful and Flask-SQLAlchemy all talking.
"""
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, pre_load

from build.config import DB_URI, DB_TRACK


# App configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DB_TRACK
db = SQLAlchemy(app)
api = Api(app)


# Model(s)
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


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    username = fields.String()
    password = fields.String()

    @pre_load
    def make_user(self, data):
        return User(**data)


# Initialize data tables
db.drop_all()
db.create_all()


class UserResource(Resource):

    def get(self):
        users_schema = UserSchema(many=True)
        users = User.query.all()
        response = users_schema.dump(users)
        return {'users': response}, 200

    def post(self):
        json_data = request.get_json()
        user = User(
            first_name=json_data['first_name'],
            last_name=json_data['last_name'],
            email=json_data['email'],
            username=json_data['username'],
            password=json_data['password']
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'user {} created!'.format(user.username)}, 201



api.add_resource(UserResource, '/users')


if __name__ == '__main__':
    app.run(debug=True)
