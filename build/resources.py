from flask import request
from flask_restful import Resource
from build.app import db
from build.models import User
from build.serializers import UserSchema

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