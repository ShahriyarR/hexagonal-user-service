from marshmallow import EXCLUDE, Schema, fields


class UserCreateDTO(Schema):
    full_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE
