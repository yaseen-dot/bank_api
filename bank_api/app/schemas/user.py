from marshmallow import Schema, fields

class UserRegisterSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class UserOutSchema(Schema):
    id = fields.Int()
    username = fields.Str()
