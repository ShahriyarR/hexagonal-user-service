from marshmallow import EXCLUDE, Schema, fields, validate, validates

from userservice.domain.model.domain import Password


class UserCreateDTO(Schema):
    full_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.Raw(required=True)

    @validates("password")
    def validate_password_type(self, value):
        if not isinstance(value, Password):
            raise TypeError("Wrong password type was provided!")

    class Meta:
        unknown = EXCLUDE
