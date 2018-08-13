from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)
from build.app import db
from build.models import User, Model
from build.serializers import UserSchema, ModelSchema


class UserResource(Resource):

    @jwt_required
    def get(self):
        users_schema = UserSchema(many=True)
        users = User.query.all()
        response = users_schema.dump(users)
        return {'users': response}, 200

    def post(self):
        if not request.is_json:
            return {"message": "The request must be in JSON format"}
        data = request.get_json()

        # Check if username already exists
        username = User.query.filter_by(username=data['username']).first()
        if username:
            return {"message": "This username already exists"}, 409
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()

        # Create JWT token for new user
        access_token = create_access_token(identity=username)
        return {
            "message": "Added user {}".format(new_user.username),
            "token": access_token
        }, 201

    def put(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

