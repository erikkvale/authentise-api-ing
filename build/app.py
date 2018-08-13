"""
A small starter app to get Flask, Flask-RESTful and Flask-SQLAlchemy all talking.
"""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from build.config import DB_URI, DB_TRACK, JWT_SECRET_KEY


# App configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DB_TRACK
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

from build.resources import UserResource, ModelResource

# Initialize data tables
db.drop_all()
db.create_all()

# API resource endpoints
api.add_resource(UserResource, '/users')
api.add_resource(ModelResource, '/models')


if __name__ == '__main__':
    app.run(debug=True)
