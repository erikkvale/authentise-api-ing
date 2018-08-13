from marshmallow import Schema, fields

class UserSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    email = fields.String()
    username = fields.String()
    password = fields.String()