from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)


class UserHello(Resource):

    def get(self):
        return {'Hello': 'world'}

api.add_resource(UserHello, '/')


if __name__ == '__main__':
    app.run(debug=True)