"""
A small starter app to get Flask, Flask-RESTful and Flask-SQLAlchemy all talking.
"""
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from build.config import DB_URI, DB_TRACK


# App configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DB_TRACK
db = SQLAlchemy(app)
api = Api(app)


from build.models import User
from build.serializers import UserSchema

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
        username = User.query.filter_by(username=json_data['username']).first()
        if username:
            return {'message': 'username already exists!'}, 409
        else:
            user = User(**json_data)
            db.session.add(user)
            db.session.commit()
            return {'message': 'user {} created!'.format(user.username)}, 201



api.add_resource(UserResource, '/users')


if __name__ == '__main__':
    app.run(debug=True)
