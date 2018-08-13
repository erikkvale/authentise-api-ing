from marshmallow import Schema, fields


class UserSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    email = fields.String()
    username = fields.String()
    password = fields.String()


class ModelSchema(Schema):
    name = fields.String()
    surface_area = fields.Float()
    volume = fields.Float()
    size_x = fields.Float()
    size_y = fields.Float()
    size_z = fields.Float()
    created_on = fields.DateTime()
    user_id = fields.Integer()